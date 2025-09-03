import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Get input values
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Simple Interest
        si = (principal * rate * time) / 100

        # Compound Interest
        ci = principal * ((1 + rate / 100) ** time) - principal

        # Display the results
        result_si.config(text=f"Simple Interest: ₹{si:.2f}")
        result_ci.config(text=f"Compound Interest: ₹{ci:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Principal Amount (₹):").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate of Interest (% per annum):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time Period (years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

# Calculate Button
tk.Button(root, text="Calculate Interest", command=calculate_interest).pack(pady=15)

# Result Labels
result_si = tk.Label(root, text="Simple Interest: ₹0.00")
result_si.pack()

result_ci = tk.Label(root, text="Compound Interest: ₹0.00")
result_ci.pack()

# Start the GUI loop
root.mainloop()
