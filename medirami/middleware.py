import redis
from django.conf import settings
from django.http import JsonResponse
from time import time
import json

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.redis_client = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=0,
            decode_responses=True
        )
        self.rate_limit = 10  # Limite de 10 solicitudes
        self.window_size = 60  # En 60 segundos

    def __call__(self, request):
        user_ip = self.get_client_ip(request)
        rate_limit_key = f'rate_limit:{user_ip}'
        cache_key = f'cached_response:{user_ip}'
        current_time = time()

        # Obtener el número de solicitudes y el tiempo del primer intento
        request_count = self.redis_client.hget(rate_limit_key, 'count')
        first_request_time = self.redis_client.hget(rate_limit_key, 'first_request_time')

        # Convertir a tipo adecuado
        request_count = int(request_count or 0)
        first_request_time = float(first_request_time or current_time)

        # Depuración
        print(f"Request Count: {request_count}, First Request Time: {first_request_time}, Current Time: {current_time}")

        if current_time - first_request_time > self.window_size:
            # Nueva ventana de tiempo
            self.redis_client.hmset(rate_limit_key, {'count': 1, 'first_request_time': current_time})
            print(f"New window started for IP: {user_ip}")
        elif request_count < self.rate_limit:
            # Incrementar el conteo de solicitudes
            self.redis_client.hincrby(rate_limit_key, 'count', 1)
            print(f"Request count incremented for IP: {user_ip}")
        else:
            # Superado el límite de solicitudes
            cached_response = self.redis_client.get(cache_key)
            if cached_response:
                print(f"Returning cached response for IP: {user_ip}")
                try:
                    # Convertir el contenido de la respuesta en JSON a un diccionario
                    response_dict = json.loads(cached_response)
                    return JsonResponse(response_dict, safe=False, status=200)
                except json.JSONDecodeError:
                    print("Cached response is not valid JSON")
                    return JsonResponse({'error': 'Rate limit exceeded'}, status=429)
            else:
                print(f"No cached response found for IP: {user_ip}")
                return JsonResponse({'error': 'Rate limit exceeded'}, status=429)

        response = self.get_response(request)

        # Verificar y almacenar la respuesta en caché si es JSON
        if response['Content-Type'] == 'application/json':
            response_content = response.content.decode('utf-8')
            self.redis_client.setex(cache_key, self.window_size, response_content)
            print(f"Response cached for IP: {user_ip}")

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
