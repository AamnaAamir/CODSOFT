import tkinter as tk
import customtkinter as ctk
import math

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x450")
root.resizable(False, False)
root.configure(bg="black")


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Function to clear all entries
def clear_all():
    entry.delete(0, tk.END)


# Function to clear the last entry
def clear_entry():
    entry.delete(len(entry.get()) - 1)


def square_root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "")


def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


entry = ctk.CTkEntry(master=root, width=250, height=40, corner_radius=10, font=("Arial", 20, "bold"), fg_color="black",
                     bg_color="black", text_color="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

button_list = [
    ("AC", 1, 0), ("CE", 1, 1), ("√", 1, 2), ("%", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
]


def on_click(button_text):
    if button_text == "=":
        calculate()
    elif button_text == "AC":
        clear_all()
    elif button_text == "CE":
        clear_entry()
    elif button_text == "√":
        square_root()
    elif button_text == "%":
        percentage()
    else:
        entry.insert(tk.END, button_text)


for button_text, button_row, button_column in button_list:
    if button_text in ["AC"]:
        fg_color = "dark orange"
        text_color = "white"
    elif button_text in ["√", "%", "CE"]:
        fg_color = "white"
        text_color = "black"
    else:
        fg_color = "gray20"
        text_color = "white"

    button_widget = ctk.CTkButton(master=root, font=("Arial", 20, "bold"), text=button_text, corner_radius=10, width=60,
                                  height=60, fg_color=fg_color, text_color=text_color, command=lambda x=button_text: on_click(x))

    button_widget.grid(row=button_row, column=button_column, padx=7, pady=7)

root.mainloop()
