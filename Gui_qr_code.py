
import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def generate_qr_code():
    text = link_entry.get()
    size = int(size_entry.get())
    color = color_entry.get()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color)
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    img.save(save_path)
    qr_image = Image.open(save_path)
    qr_image.thumbnail((200, 200))
    qr_photo = ImageTk.PhotoImage(qr_image)

    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    result_label.config(text=f'QR code saved as {save_path}')

# Create a GUI window
root = tk.Tk()
root.title("QR Code Generator")

# Create GUI elements
link_label = tk.Label(root, text="Enter Link:")
link_label.pack()
link_entry = tk.Entry(root, width=40)
link_entry.pack()

size_label = tk.Label(root, text="QR Code Size:")
size_label.pack()
size_entry = tk.Entry(root, width=5)
size_entry.pack()

color_label = tk.Label(root, text="Fill Color (e.g., #6aff9b):")
color_label.pack()
color_entry = tk.Entry(root, width=10)
color_entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

qr_label = tk.Label(root)
qr_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
