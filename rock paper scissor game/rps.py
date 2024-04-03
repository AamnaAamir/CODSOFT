import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random


def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    update_scores(winner)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'


def display_result(user_choice, computer_choice, winner):
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n", fg="white")
    if winner == 'tie':
        result_label.config(text=result_label.cget('text') + "It's a tie!", fg="white")
    elif winner == 'user':
        result_label.config(text=result_label.cget('text') + "You win!", fg="white")
    else:
        result_label.config(text=result_label.cget('text') + "Computer wins!", fg="white")


def show_winner():
    result_text = result_label.cget('text')
    if "You win!" in result_text:
        winner = 'user'
    elif "Computer wins!" in result_text:
        winner = 'computer'
    else:
        winner = 'tie'

    if winner != 'tie':
        messagebox.showinfo("Winner", f"{winner.capitalize()} wins!")
    else:
        messagebox.showinfo("Winner", "It's a tie!")


def update_scores(winner):
    global user_score, computer_score
    if winner == 'user':
        user_score += 1
    elif winner == 'computer':
        computer_score += 1
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")


def replay():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    result_label.config(text="")


def exit_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    result_label.config(text="")
    m.destroy()  # Close the window


# Initialize scores
user_score = 0
computer_score = 0

# Create main window
m = tk.Tk()
m.title("RPS")
m.resizable(True, True)
m.geometry("900x900")

# Load images
rock_image = ImageTk.PhotoImage(Image.open(r"D:\rock.png").resize((120, 120)))
paper_image = ImageTk.PhotoImage(Image.open(r"D:\paper.png").resize((120, 120)))
scissors_image = ImageTk.PhotoImage(Image.open(r"D:\scissor.png").resize((120, 120)))
quit_image = ImageTk.PhotoImage(Image.open(r"D:\exit.png").resize((180, 50)))
new_image = ImageTk.PhotoImage(Image.open(r"D:\replay.png").resize((180, 50)))
result_image = ImageTk.PhotoImage(Image.open(r"D:\result.png").resize((180, 50)))
bg = Image.open(r"D:\bg.png").resize((1400, 1200))
bg_img = ImageTk.PhotoImage(bg)

bg_label = tk.Label(m, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# GUI elements
style = ttk.Style()
title_label = tk.Label(m, text="▂▃▅▇█▓▒░Gesture Showdown: RPS Edition░▒▓█▇▅▃▂", bg="black", fg="white",
                       font=("Algerian", 29, "italic", "bold"))
title_label.place(x=40, y=30)

f1 = tk.Frame(m, bg="black")
f1.place(x=720, y=150, width=450, height=400)

f2 = tk.Frame(m, bg="black")
f2.place(x=220, y=150, width=450, height=300)

f3 = tk.Frame(m, bg="black")
f3.place(x=350, y=580, width=650, height=100)

# Labels
score_board_label = tk.Label(f1, text="Score Board", font=("Times New Roman", 30, "bold", "underline"), bg="black",
                             fg="white")
score_board_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

move_label = tk.Label(f2, text="Choose your move", font=("Times New Roman", 30, "bold", "underline"), bg="black",
                      fg="white")
move_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

rock_label = tk.Label(f2, text="Rock", font=("Times New Roman", 24, "bold"), bg="black", fg="white")
rock_label.grid(row=5, column=0, columnspan=1, padx=10, pady=10)

paper_label = tk.Label(f2, text="Paper", font=("Times New Roman", 24, "bold"), bg="black", fg="white")
paper_label.grid(row=5, column=1, columnspan=1, padx=10, pady=10)

scissor_label = tk.Label(f2, text="Scissor", font=("Times New Roman", 24, "bold"), bg="black", fg="white")
scissor_label.grid(row=5, column=2, columnspan=3, padx=10, pady=10)

user_score_label = tk.Label(f1, text=f"Your Score: {user_score}", font=("Times New Roman", 24, "bold"),
                            bg="violet red", fg="white")
user_score_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

computer_score_label = tk.Label(f1, text=f"Computer Score: {computer_score}", font=("Times New Roman", 24, "bold"),
                                bg="DeepSkyBlue2", fg="white")
computer_score_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

result_label = tk.Label(f1, text="", font=("Times New Roman", 24, "bold"), bg="black", fg="white")
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Buttons
rock_button = tk.Button(f2, image=rock_image, command=lambda: play_game("rock"), bg="violet red")
rock_button.grid(row=3, column=0, padx=10, pady=5)

paper_button = tk.Button(f2, image=paper_image, command=lambda: play_game("paper"), bg="DeepSkyBlue2")
paper_button.grid(row=3, column=1, padx=10, pady=5)

scissors_button = tk.Button(f2, image=scissors_image, command=lambda: play_game("scissors"), bg="medium orchid")
scissors_button.grid(row=3, column=2, padx=10, pady=5)

replay_button = tk.Button(f3, image=new_image, command=replay, bg="DeepSkyBlue2")
replay_button.grid(row=2, column=3, padx=20, pady=20)

quit_button = tk.Button(f3, image=quit_image, command=exit, bg="DeepSkyBlue2")
quit_button.grid(row=2, column=4, padx=20, pady=20)

result_button = tk.Button(f3, image=result_image, command=show_winner, bg="DeepSkyBlue2")
result_button.grid(row=2, column=5, columnspan=20, pady=20)

# Run main event loop
m.mainloop()
