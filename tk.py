import tkinter as tk
import random 


def winner(user_choice):
    choice = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choice)

    if user_choice == computer_choice:
        result =  "its a tie"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"

    #update the label 
    result_label.config(text= f"{result} \nComputer Choice = {computer_choice}, player choice = {user_choice}")

root = tk.Tk()
root.title("rock paper sizzor game")

#create the buttons: 
rock_button = tk.Button(root, text = "rock", command= lambda: winner('Rock'), width= 10)
paper_button = tk.Button(root, text = "paper", command= lambda: winner('Paper'), width= 10)
scissors_button = tk.Button(root, text = "scissors", command= lambda: winner('Scissors'), width= 10)

result_label = tk.Label(root, text="")

# Layout the buttons and label
rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()