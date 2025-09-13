import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)
    
    if length == 0:
        strength = "Please enter a password"
    elif length < 4:
        strength = "Very Weak"
    elif length < 8:
        strength = "Weak"
    elif length < 12:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    # Show result in label
    result_label.config(text=f"Password Strength: {strength}")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

# Widgets
label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()