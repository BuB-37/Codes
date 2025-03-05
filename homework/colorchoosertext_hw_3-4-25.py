import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Color Text Box")

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_label.config(fg=color)

def update_text():
    text_label.config(text=user_input.get())


user_input = tk.Entry(root, width=40)
user_input.pack(pady=10)

text_label = tk.Label(root, text="COLORED TEXT")
text_label.pack(pady=10)

color_button = tk.Button(root, text="Chose Color", command=choose_color)
color_button.pack(pady=5)

update_button = tk.Button(root, text="Update the writing/text", command=update_text)
update_button.pack(pady=5)

root.mainloop()
