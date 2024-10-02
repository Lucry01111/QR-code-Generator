import qrcode
from PIL import Image

def generate_qr_code(data):
    # Crea il QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Crea l'immagine del QR code
    img = qr.make_image(fill='black', back_color='white')

    # Mostra l'immagine del QR code a schermo
    img.show()

    # Chiedi se l'utente vuole scaricare l'immagine
    save_option = input("Vuoi scaricare il QR code? (s/n): ")

    if save_option.lower() == 's':
        # Chiedi il nome del file
        filename = input("Inserisci il nome del file (esempio: my_qr_code.png): ")
        img.save(filename)
        print(f"QR code salvato come {filename}")
    else:
        print("QR code non salvato.")

# Genera un QR code con dati personalizzati
generate_qr_code("https://www.example.com")
