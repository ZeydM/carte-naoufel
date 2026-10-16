# Installer : pip install "qrcode[pil]"
import qrcode

url = input("Colle le lien complet de ta page GitHub Pages : ").strip()
if not url.startswith("https://"):
    raise ValueError("Le lien doit commencer par https://")
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=14,border=4)
qr.add_data(url)
qr.make(fit=True)
qr.make_image(fill_color="black",back_color="white").save("QR_Naoufel_Mrini.png")
print("QR_Naoufel_Mrini.png créé. Teste-le sur un téléphone avant impression.")
