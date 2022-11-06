from sys import exit

players = 4


def total(players):
    players = (players - 1)
    print(players)



def yellow_room():
    print("In front of you is a door to your left and a door directly ahead.")
    print("The door on your left says NO ENTRY.")
    print("Do you go left or straight")

    choice = input(">  ")

    if choice == "left":
        dead("A player has been eaten by Cthuhlu")
    if dead:
        print("players are left", total(players))

    if "ahead" or "straight" in choice:
        print("You have escaped! Congrats!")

def blue_room():
    print("In front of you is a door to your left and a door directly ahead.")
    print("The door on your left says NO ENTRY.")
    print("Do you go left or straight")

    choice = input(">  ")

    if choice == "left":
        dead("A players head has been cut off by a katana")
    if killed:
        print("A player has been killed")

    if "ahead" or "straight" in choice:
        green_room()

def green_room():
    print("In front of you is a door to your left and a door directly ahead.")
    print("The door on your left says NO ENTRY.")
    print("Do you go left or straight")

    choice = input(">  ")

    if choice == "left":
        dead("A players head has been cut off by a katana")
    if dead:
        print(players - 1, "players are left")
        green_room()

    if "ahead" or "straight" in choice:
        yellow_room()

def dead(why):
    if total(players) == 0:
        print(why, "Good job.")
        exit(0)

def killed(why):
    print(why, "Good job.")
    print(total(players))

def start():
    print("You've been dropped off in a red room and given a set of rules.")
    print("You have 3 other people with you.")
    print("The rules are: You have to choose the right door or someone dies.")
    print("If you get to the end, you live. There are 4 rooms total.")
    print("In front of you is a door to your left and a door directly ahead.")
    print("The door on your left says NO ENTRY.")
    print("Do you go left or straight")

    choice = input(">  ")

    if choice == "left":
       killed("A player has been burned by acid")

    if "ahead" or "straight" in choice:
        blue_room()


start()
