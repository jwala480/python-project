import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def get_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!" 
    else:
        return "Computer wins!"

def play_game():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()

    print("Computer chose:", computer_choice)
    result = get_winner(user_choice, computer_choice)
    print(result)

play_game()