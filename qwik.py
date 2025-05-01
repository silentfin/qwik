# Qwik - qr code generator

import qrcode
import os
import argparse
from datetime import datetime
import webbrowser

def validate_input(data):
    if not data.strip():
        raise ValueError("Input cannot be empty")
    if len(data) > 2953: 
        raise ValueError("Input too long (max 2953 characters)")
    return data

def generate_qr(data, output_dir="qr_codes", color="black", size=10, border=4):

    #test input
    data = validate_input(data)
    
    #generating directory to store the qr images
    os.makedirs(output_dir, exist_ok=True)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"qr_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    # Create and save QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color="white")
    img.save(filepath)

    return filepath    
    

def main():
    parser = argparse.ArgumentParser(description='Generate customizable QR codes')
    parser.add_argument('data', help='Text or URL to encode')
    parser.add_argument('--output-dir', default="qr_codes", help='Output directory (default: qr_codes)')
    parser.add_argument('--color', default="black", help='QR code color (default: black)')
    parser.add_argument('--size', type=int, default=10, help='Pixel size per module (default: 10)')
    parser.add_argument('--border', type=int, default=4, help='White border thickness (default: 4)')
    parser.add_argument('--open', action='store_true', help='Auto-open generated QR code')   
    
    args = parser.parse_args()
    
    try:
        saved_path = generate_qr(
            args.data,
            output_dir=args.output_dir,
            color=args.color,
            size=args.size,
            border=args.border
            )

        print(f"QR code generated successfully at:\n{saved_path}")

        if args.open:
            webbrowser.open(saved_path)

    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    main()