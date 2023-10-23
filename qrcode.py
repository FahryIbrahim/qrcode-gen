import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)
url=input("Enter the URL: ")
user_have_logo=input("Do you have a logo? (y/n): ").strip().lower()
qr.add_data(url)
qr.make(fit=True)
if(user_have_logo=="y"):
    logo=input("Enter the logo path: ")
    qr_img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=logo)
else:
    custom_color=input("Do you want to change the color? (y/n): ").strip().lower()
    if(custom_color=="y"):
        foreground_color=input("Enter the foreground color: ")
        background_color=input("Enter the background color: ")
        qr_img = qr.make_image(fill_color=foreground_color, back_color=background_color)
    else:
        qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("qr.png")