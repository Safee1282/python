import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        # Get values from entry boxes
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())

        today = date.today()
        dob = date(y, m, d)

        # Calculate age
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        messagebox.showinfo("Age Calculator", f"Your present age is {age} years.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for day, month, and year.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Tkinter Window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

# Labels and Entry boxes
tk.Label(root, text="Enter Date of Birth", font=("Arial", 12, "bold")).pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Day:").grid(row=0, column=0, padx=5)
day_entry = tk.Entry(frame, width=5)
day_entry.grid(row=0, column=1)

tk.Label(frame, text="Month:").grid(row=0, column=2, padx=5)
month_entry = tk.Entry(frame, width=5)
month_entry.grid(row=0, column=3)

tk.Label(frame, text="Year:").grid(row=0, column=4, padx=5)
year_entry = tk.Entry(frame, width=7)
year_entry.grid(row=0, column=5)

# Button
tk.Button(root, text="Calculate Age", command=calculate_age, bg="lightblue").pack(pady=10)

root.mainloop()
