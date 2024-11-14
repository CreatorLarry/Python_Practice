import random

print("Welcome to Python's Rock/Paper/Scissors Game \033[1mWith Larry!\033[0m")

user_input_consent = input("To continue, Press C. To quit, press Q: ")
if user_input_consent.lower() == "c":
    print("Yeeeey! Let's play!")
elif user_input_consent.lower() == "q":
    print("You are welcome next time. Byeeee.")
    quit()
else:
    print("Please enter either C or Q. Run again.")
    quit()

# scores
user_wins = 0
computer_wins = 0
tied_times = 0

# options
options = ["rock", "paper", "scissors"]

# Limit the game to 6 rounds
rounds_played = 0
total_rounds = 6

while rounds_played < total_rounds:
    user_input = input("Type either Rock, Paper or Scissors: ").lower()
    if user_input not in options:
        print("Please enter either Rock, Paper or Scissors.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer pick is {computer_pick}.")

    if user_input == 'rock' and computer_pick == 'scissors':
        print("You win!")
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You win!")
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You win!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Tie!")
        tied_times += 1
    else:
        print("You lose!")
        computer_wins += 1

    rounds_played += 1
    print(f"Round {rounds_played} of {total_rounds} complete.")

# Display the final score after 6 rounds
print(f"\nFinal Scores:\nYou won {user_wins} times.\nThe computer won {computer_wins} times. \nYou tied {tied_times} times")
print("Play again when you can. \nGoodbye.")
