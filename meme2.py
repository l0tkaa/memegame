# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
lives = 4


def yellow_room(lives):
    print("Yellow Room. In front of you is a door to your left and a door directly ahead.")
    print("The door on your left says NO ENTRY.")
    print("Do you go left or straight")

    choice = input(">  ")

    if choice == "left":
        lives -= 1
        print("nay, try again, you have", lives, "lives left")

    if "ahead" or "straight" in choice:
        print("You have escaped! Congrats!")


def green_room(lives):
    print("Green Room. In front of you is a door to your left and a door directly ahead.")
    print("The door on your left says NO ENTRY.")
    print("Do you go left or straight")

    choice = input(">  ")

    if choice == "left":
        lives -= 1
        print("nay, try again, you have", lives, "lives left")

    if "ahead" or "straight" in choice:
        yellow_room(lives)


def blue_room(lives):
    print("Blue Room. In front of you is a door to your left and a door directly ahead.")
    print("The door on your left says NO ENTRY.")
    print("Do you go left or straight")
    choice = input(">  ")
    if choice == "left":
        lives -= 1
        print("nay, try again, you have", lives, "lives left")

    if choice == "straight":
        print("yay, you advance! Move to green room")
        green_room(lives)


def main():
    # The setup
    lives = 4
    right_answer = "straight"

    print(
        "You've been dropped off in a red room and given a set of rules.\nYou have 3 other people with you.\n The rules are: You have to choose the right door or someone dies.\nIf you get to the end, you live. There are 4 rooms total.\nIn front of you is a door to your left and a door directly ahead.\nThe door on your left says NO ENTRY.\nDo you go left or straight")

    # The game
    while lives > 0:
        choice = input("straight or left:")
        if choice == right_answer:
            print("yay, you advance! Move to blue room")
            blue_room(lives)
            print(
                "Blue Room. In front of you is a door to your left and a door directly ahead.\nThe door on your left says NO ENTRY. \nDo you go left or straight")




        else:
            lives -= 1
            print("nay, try again, you have", lives, "lives left")
    else:
        print("you lose")


# This will call our function and run the game
if __name__ == "__main__":
    main()
