import base64
from PIL import Image
from io import BytesIO

from suds.client import Client

c = Client('http://127.0.0.1:8000/Producer?wsdl')
data = c.service.XRoad(1000)
image = c.service.ImageDownload(1000)


im = Image.open(BytesIO(base64.b64decode(image)))
im.save(f'image{1000}.png', 'PNG')
