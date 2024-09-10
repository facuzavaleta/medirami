import redis
from django.conf import settings
from django.http import JsonResponse

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.redis_client = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDISPASSWORD,
            db=0,
            decode_responses=True
        )
        self.rate_limit = 15  # Límite de 7 solicitudes
        self.window_size = 15  # Ventana de 30 segundos

    def __call__(self, request):
        user_ip = self.get_client_ip(request)
        rate_limit_key = f'rate_limit:{user_ip}'

        try:
            # Incrementar el contador y establecer la expiración si es una nueva clave.
            request_count = self.redis_client.incr(rate_limit_key)

            # Si es la primera solicitud, establecer la expiración.
            if request_count == 1:
                self.redis_client.expire(rate_limit_key, self.window_size)
                print(f"New window started for IP: {user_ip}, count set to 1")

            # Si el límite de solicitudes ha sido alcanzado, devolver un error 429.
            if request_count > self.rate_limit:
                print(f"Rate limit exceeded for IP: {user_ip}, returning 429")
                return JsonResponse({'error': 'Rate limit exceeded'}, status=429)

        except redis.exceptions.ResponseError as e:
            # Captura el error y limpia la clave si hay un tipo incorrecto
            print(f"Redis ResponseError: {e}. Resetting key for IP: {user_ip}")
            self.redis_client.delete(rate_limit_key)
            # Reiniciar el contador tras limpieza
            self.redis_client.setex(rate_limit_key, self.window_size, 1)

        # Continúa con la solicitud si el límite no se ha alcanzado.
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip