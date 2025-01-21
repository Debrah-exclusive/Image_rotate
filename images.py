import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    """Open an image file and display it in the GUI."""
    global image_path
    global image
    global image_label
    image_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.png;*.jpeg;*.bmp;*.gif")]
    )
    if image_path:
        image = Image.open(image_path)
        display_image()

def display_image():
    """Display the current image in the GUI."""
    global image
    global image_label
    img_display = ImageTk.PhotoImage(image)
    image_label.config(image=img_display)
    image_label.image = img_display

def rotate_yes():
    """Rotate the current image by 90°."""
    global image
    global image_label
    if image:
        image = image.rotate(90)
        display_image()

def rotate_no():
    """Reset the rotation of the current image."""
    global image
    global image_label
    image = Image.open(image_path)
    display_image()

def main():
    global image_label
    root = tk.Tk()
    image_label = tk.Label(root)
    image_label.pack()

    open_button = tk.Button(root, text="Open Image", command=open_image)
    open_button.pack()

    rotate_button_frame = tk.Frame(root)
    rotate_button_frame.pack()

    rotate_yes_button = tk.Button(rotate_button_frame, text="Rotate 90°", command=rotate_yes)
    rotate_yes_button.pack(side=tk.LEFT)

    rotate_no_button = tk.Button(rotate_button_frame, text="Reset Rotation", command=rotate_no)
    rotate_no_button.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()