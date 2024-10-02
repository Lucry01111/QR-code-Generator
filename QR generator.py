import qrcode
from PIL import Image
import os

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill='black', back_color='white')
    img.show()

    save_option = input("Do you want to download the QR code? (y/n): ")

    if save_option.lower() == 'y':
        filename = input("Enter the file name (without extension, e.g., my_qr_code): ")
        valid_extensions = ['.png', '.jpg', '.jpeg']
        file_ext = input("Enter the desired extension (.png, .jpg, .jpeg): ").lower()

        # If the extension is not valid, use '.png' as default
        if file_ext not in valid_extensions:
            print("Invalid extension, using '.png' by default.")
            file_ext = '.png'
        # Combine the file name and extension
        full_filename = filename + file_ext
        # Specific path for saving
        save_path = os.path.join(r'C:\Users\lucre\Documents\Codici Vari\Python\QR code', full_filename)

        # Save the QR code image
        img.save(save_path)
        print(f"QR code saved as {save_path}")
    else:
        print("QR code not saved.")
data = input("Enter the link for the QR code: ")
generate_qr_code(data)
