import tkinter as tk
from tkinter import ttk 

fruit = tk.Tk()
fruit.title("Fruit")

label = tk.Label(fruit,text="Select a Fruit:")
label.pack(pady=10)

options = ["Watermellon","Mango","Banana"]
dropdown= ttk.Combobox(fruit,values=options)
dropdown.set("Choose a Fruit")
dropdown.pack(pady=10)

def show_selection():
    selected_option= dropdown.get()
    result_label.config(text=f"You selected: {selected_option}")

button = tk.Button(fruit,text="Submit",command=show_selection)
button.pack(pady=10)

result_label=tk.Label(fruit,text="")
result_label.pack(pady=10)

fruit.mainloop()

#Second Drop Down
color = tk.Tk()
color.title("Color")

label = tk.Label(color,text="Select a Color:")
label.pack(pady=10)

options = ["Blue","Red","Green"]
dropdown= ttk.Combobox(color,values=options)
dropdown.set("Choose a Color")
dropdown.pack(pady=10)

def show_selection():
    selected_option= dropdown.get()
    result_label.config(text=f"You selected: {selected_option}")

button = tk.Button(color,text="Submit",command=show_selection)
button.pack(pady=10)

result_label=tk.Label(color,text="")
result_label.pack(pady=10)

color.mainloop()