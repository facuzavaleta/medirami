import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

def generar_codigo_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format='PNG')  # Guardamos la imagen en formato PNG en el buffer

    filename = 'codigo_qr.png'

    # Guardamos el contenido del buffer en un archivo File de Django
    filebuffer = File(buffer, name=filename)

    return filebuffer