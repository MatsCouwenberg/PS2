# Imports
from pyzbar.pyzbar import decode
from PIL import Image

# Open webcam and scan QR codes
image_path = 'qr.png'
img = Image.open(image_path)

# Decode the QR code
decoded_objects = decode(img)

# Output the data and the orientation if QR code is scanned
if decoded_objects:
    qr_code = decoded_objects[0]
    orientation = qr_code.orientation
    data = qr_code.data.decode('utf-8')
    print(f"Orientatie: {orientation}")
    print(f"Data: {data}")
else:
    print("No QR code found in the image")

