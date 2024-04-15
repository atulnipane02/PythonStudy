import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
canvas = tk.Canvas(root, width=900, height=600, bg='white')
canvas.grid(columnspan=3)


logo = Image.open('rockpaperscissorImage.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)
root.mainloop()
