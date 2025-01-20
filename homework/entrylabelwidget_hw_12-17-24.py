import tkinter as tk 
from tkinter import ttk

def show_input():
    user_input = entry.get()
    label_result.config(text=f"You entered : {user_input}")

bob = tk.Tk()
bob.title("Info")

label_p=tk.Label(bob, text="Enter your name : ")
label_p.pack(pady=5)

entry = tk.Entry(bob, width=30)
entry.pack(pady=5)

button_sub = tk.Button(bob, text="Submit", command=show_input)
button_sub.pack(pady=5)

label_result= tk.Label(bob, text="")
label_result.pack(pady=5)

label = tk.Label(bob, text="Choose your age:")
label.pack(pady=10)

options = ["13","14","15"]
dropdown = ttk.Combobox(bob,values=options)
dropdown.set("Choose an option")
dropdown.pack(pady=10)

def show_selection():
    selected_option = dropdown.get()
    result_label.config(text=f"You selected: {selected_option}")

button = tk.Button(bob,text="Submit",command=show_selection)
button.pack(pady=10)

result_label = tk.Label(bob,text="")
result_label.pack(pady=10)

bob.mainloop()
