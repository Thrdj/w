#QR Code using Python
#stuck pyqrcode not working#
import pyqrcode
import png
link = "https://www.w3schools.com/python/"
qr_code = pyqrcode.create(link)
qr_code.png("qrcode_www.w3schools.com.png", scale=5)

#Decode a QR Code using Python
from pyzbar.pyzbar import decode
from PLT import Image
decocdeQR = decode(Image.open('qrcode_www.w3schools.com.png'))
print(decocdeQR[0].data.decode('ascii'))

#clcoding.com