import base64
import sys
from PIL import Image
from io import BytesIO
from suds.client import Client

c = Client('http://127.0.0.1:8000/Producer?wsdl')
data = c.service.XRoad(sys.argv[1])
image = c.service.ImageDownload(sys.argv[1])


im = Image.open(BytesIO(base64.b64decode(image)))
im.save(f'image{sys.argv[1]}.png', 'PNG')