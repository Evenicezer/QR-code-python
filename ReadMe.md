# QR Code Generator

This is a simple Python script for generating QR codes using the `qrcode` library.

## Usage

1. Make sure you have the `qrcode` library installed. You can install it using pip:

pip install qrcode[pil]

2. Use the `generate_qr_code` function to generate a QR code from a text input.

```python
text = 'www.gitlab.com/Evenezer'
file_name = 'qr_code.png'
generate_qr_code(text, file_name)
The QR code will be generated and saved as qr_code.png in the current working directory.
Error Correction Levels
The QR code generated has a specified error correction level which can be adjusted in the code. By default, it uses medium error correction (M), which can correct about 15% or less errors. You can modify the error correction level in the generate_qr_code function based on your needs.

## Dependencies
qrcode library for generating QR codes.
Pillow library for rendering the QR code image.
License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
The qrcode library developers for creating a simple and efficient tool for generating QR codes.
The Pillow library developers for providing the image rendering capabilities.
