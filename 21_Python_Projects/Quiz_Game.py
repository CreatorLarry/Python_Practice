print("Welcome to \033[1mLarry's Quiz Game!\033[0m")

playing = input("Do you want to Play? (yes) or (no)   ")
if playing.lower() != "yes":
    print("Ooops, too bad, Maybe next time!")
    quit()
print("Okay! Lets play ; ")

print("1. 5 Wed-Dev Acronyms \n2. 6 Proverbs with Larry \n3. 5 Questions You should know answers to")

game_play = input("Enter Number of Game you'd like to play :) ")
# keeping score
score = 0

# Game 1
if game_play == "1":
    print("Welcome to the 5 Wed-Dev Acronyms Quiz Game! \nAll the best.")
    answer = input("What does SQL stand for? ").lower()
    if answer == "structured query language":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is: structured query language.")

    answer = input("What does HTML stand for? ").lower()
    if answer == "hypertext markup language":
        print("Correct! ")
        score += 1
    else:
        print("Incorrect! \n correct answer is: hypertext markup language.")

    answer = input("What does CSS stand for? ").lower()
    if answer == "cascading style sheets":
        print("Correct! ")
        score += 1
    else:
        print("Incorrect! \n correct answer is: cascading style sheets.")

    answer = input("What does DOM stand for? ").lower()
    if answer == "document object model":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is: document object model.")

    answer = input("What does IDE stand for? ").lower()
    if answer == "integrated development environment":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is: integrated development environment.")

# Game 2
elif game_play == "2":
    print("Welcome to the 6 Proverbs with Larry Quiz Game! \nAll the best.")
    answer = input("The early bird ").lower()
    if answer == "catches the worm":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is: \033[1mThe early bird\033[0m catches the worm.")

    answer = input("Cleanliness is ").lower()
    if answer == "next to Godliness":
        print("Correct! ")
        score += 1
    else:
        print("Incorrect! \n correct answer is: \033[Cleanliness is\033[0m next to Godliness.")

    answer = input("Strike while ").lower()
    if answer == "the iron is hot":
        print("Correct! ")
        score += 1
    else:
        print("Incorrect! \n correct answer is: \033[1mStrike while\033[0m the iron is hot.")

    answer = input("Don't count your chickens ").lower()
    if answer == "before they hatch":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is: \033[1mDon't count your chicken\033[0m before they hatch.")

    answer = input("Look before ").lower()
    if answer == "you leap":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is:  \033[1mLook before\033[0m you leap.")

    answer = input("Every cloud ").lower()
    if answer == "has a silver lining":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is:  \033[1mEvery cloud \033[0m has a silver lining.")

# Game 3
elif game_play == "3":
    answer = input("The early bird ").lower()
    if answer == "catches the worm":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is: \033[1mThe early bird\033[0m catches the worm.")

    answer = input("Cleanliness is ").lower()
    if answer == "next to Godliness":
        print("Correct! ")
        score += 1
    else:
        print("Incorrect! \n correct answer is: \033[Cleanliness is\033[0m next to Godliness.")

    answer = input("Strike while ").lower()
    if answer == "the iron is hot":
        print("Correct! ")
        score += 1
    else:
        print("Incorrect! \n correct answer is: \033[1mStrike while\033[0m the iron is hot.")

    answer = input("Don't count your chickens ").lower()
    if answer == "before they hatch":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is: \033[1mDon't count your chicken\033[0m before they hatch.")

    answer = input("Look before ").lower()
    if answer == "you leap":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! \n correct answer is:  \033[1mLook before\033[0m you leap.")
# printing score
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + " %.")
