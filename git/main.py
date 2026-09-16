def treasure_game(choice1, choice2, choice3):
    if choice1 == "left":
        if choice2 == "wait":
            if choice3 == "green":
                return "You found the TREASURE!"
            elif choice3 == "red":
                return "Game Over!"
            elif choice3 == "blue":
                return "Game Over!"
            else:
                return "Invalid choice!"
        else:
            return "Game Over!"
    else:
        return "Game Over!"


if __name__ == "__main__":
    print("🏝️ Welcome to Treasure Island!")

    choice1 = input("LEFT or RIGHT? ").lower()
    choice2 = input("SWIM or WAIT? ").lower()
    choice3 = input("RED, BLUE, or GREEN? ").lower()

    print(treasure_game(choice1, choice2, choice3))