import tkinter as tk
import random

# ---------- Game Logic ----------
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        scores["User"] += 1
    else:
        result = "Computer Wins!"
        scores["Computer"] += 1

    # Update labels
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score → You: {scores['User']} | Computer: {scores['Computer']}")

def reset_game():
    scores["User"] = 0
    scores["Computer"] = 0
    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer's Choice: ")
    result_label.config(text="Result: ")
    score_label.config(text="Score → You: 0 | Computer: 0")

# ---------- Main Window ----------
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x350")
root.config(bg="#f0f0f0")

scores = {"User": 0, "Computer": 0}

# Labels
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14), bg="#f0f0f0")
user_label.pack()

computer_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14), bg="#f0f0f0")
computer_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 16, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 14, "bold"), bg="#f0f0f0")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=12, height=2, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=12, height=2, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=12, height=2, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=5, pady=5)
paper_btn.grid(row=0, column=1, padx=5, pady=5)
scissors_btn.grid(row=0, column=2, padx=5, pady=5)

reset_btn = tk.Button(root, text="Reset Score", width=15, height=2, command=reset_game, bg="orange")
reset_btn.pack(pady=15)

root.mainloop()
