import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Get numbers from entry fields
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        
        # Display result in label
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200")

# Labels and entries
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Button to calculate
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="Product: ")
result_label.pack(pady=5)

# Run the application
root.mainloop()