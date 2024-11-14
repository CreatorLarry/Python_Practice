# if,elif and else
print(
    "Adventure Story \nIntro: You,the player are on a quest to find a hidden treasure in a mysterious forest. You will face choices at each stage, and only one path leads to the treasure.")
name = input("Wanna play? Enter your name Friend")
print(f"Welcome {name}. All the best")
# Game begins
answer = input(
    "You arrive at the edge of a dark forest. To your left is a well-worn path, while to your right is a narrow, overgrown trail with thorny bushes. Which path do you choose? (valid answers left or right) ").lower()
# Level 1
if answer == "left":
    answer = input(
        "Level 1 complete \nDeeper into the forest, you come across a fork in the road. To the left, the path goes down into a misty valley. To the right, the path leads up a steep hill. Which path do you take? (valid answers left or right)")

    if answer == "left":
        print("")

    elif answer == "walk":
        print("Yeeey!!! After walking so many miles, you made it to the bridge and safely crossed it. Cudos!!")

    else:
        print("That's not a valid option. Try again ")

elif answer == "right":
    answer = input(
        "A river, calm as a millpond, flow in the way to the other side. You can either swim across it or walk around it to a distant bridge. Enter\033[1m swim\033[0m to swim across or\033[1m walk\033[0m to walk around it")

    if answer == "swim":
        print("Ooops! You swam and the camouflaged alligators had a delicious meal of you. Try again next time.")

    elif answer == "walk":
        print("Yeeey!!! After walking so many miles, you made it to the bridge and safely crossed it. Cudos!!")

    else:
        print("That's not a valid option. Try again ")

else:
    print("That's not a valid option. Try again")

print(f"Thank you {name} for playing!")
