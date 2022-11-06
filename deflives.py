def main():
    # The setup
    right_answer = "straight"
    lives = 4

    # The game
    while lives > 0:
        choice = input("straight or left:")
        if choice == right_answer:
            print ("yay, you win!")
            break
        else:
            lives -= 1
            print ("nay, try again, you have", lives, "lives left")
    else:
        print ("you lose")

# This will call our function and run the game
if __name__ == "__main__":
    main()
