# if,elif and else
print(
    "Adventure Story \nIntro: You,the player are on a quest to find a hidden treasure in a mysterious forest. You will face choices at each stage, and only one path leads to the treasure.")
name = input("Wanna play? Enter your name Friend: ")
print(f"Welcome {name}. All the best \nWelcome to Stage One")
# Game begins
# Stage I - Entering the forest
answer = input(
    "You arrive at the edge of a dark forest. To your left is a well-worn path, while to your right is a narrow, overgrown trail with thorny bushes. Which path do you choose? \n(valid answers left or right) ").lower()

# Stage 2
if answer == "left":
    print("Good Choice! This path is safe and takes you deeper into the forest. Stage One Complete \n\033[Welcome to stage 2\033[0m")
    answer = input(
        "Deeper into the forest, you come across a fork in the road. To the left, the path goes down into a misty valley. To the right, the path leads up a steep hill. Which path do you take? \n(valid answers left or right)").lower()

    # Stage 3
    if answer == "right":
        print(
            "Yeeey! The high ground is safer and offers a better view of your surroundings. Cudos! Stage Two Complete \n\033[Welcome to stage 3\033[0m")
        answer = input(
            "You reach a river with a gentle current. You see a sturdy-looking bridge on one side and a rickety old raft on the other. How will you cross the river? \nType 'bridge' to cross the bridge or 'raft' to take the raft.").lower()

    # Stage 4
        if answer == "bridge":
            print("Amazing! The bridge is stable, leading you safely across the river. Cudos! Stage Three Complete \n\033[Welcome to stage 4\033[0m")
            input("After crossing the bridge, you spot a cave with faint light flickering inside. To the right of the cave, there's a path leading up a cliff. Will you enter the cave to investigate or climb up the cliff? \nType 'cave' to enter the cave or 'cliff' to climb the cliff.")

            if answer == "cave":
                print()

            elif answer == "cliff":
                print("Unfortunately, results in a dead end with no way forward. You lose!")

            else:
                print("That's not a valid option. Try again")


        elif answer == "raft":
            print("Nooooo. Choosing the raft causes it to fall apart halfway into the river, making you lose.")

        else:
            print("That's not a valid option. Try again")

    elif answer == "left":
        print("Ooooops! This leads you into a hidden swamp, where you sink and lose.")

    else:
        print("That's not a valid option. Try again ")

elif answer == "left":
    print("Oooops! This leads you into a dense area where you get stuck and lose.")

else:
    print("That's not a valid option. Try again")

print(f"Thank you {name} for playing!")
