# importing random module
import random
print("Welcome to The Number Guessing Game \033[1mWith Larry!\033[0m!")
# define number to be guessed
top_of_range = input('Type the Maximum Number you would like to guess: ')

# if statement to ensure value entered (which is a string according to python) is an integer and greater than 1
if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # converting the value into an integer
    if top_of_range <= 0:
        print('Please type a number greater than 0 next time.')
        quit()

else:
    print('Please type a number.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)  # converting the value into an integer
        if top_of_range <= 0:
            print('Please type a number greater than 0 next time.')
            quit()

    else:
        print('Please type a number.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break

    elif user_guess > random_number:
        print('Your guess is higher than the number.')

    else:
        print('Your guess is lower than the number.')

print(f'You have made {guesses} guesses.')
