import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry_inch.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Input label and entry
label_prompt = tk.Label(root, text="Enter length in inches:")
label_prompt.pack(pady=5)

entry_inch = tk.Entry(root)
entry_inch.pack(pady=5)

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_to_cm)
button_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

# Run the app
root.mainloop()