import qrcode 
from PIL import Image

qr= qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H)

qr.add_data("google.com")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color = "blue")
img.save("Google.com.PNG")