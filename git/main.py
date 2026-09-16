print("🏝️ Welcome to the Treasure Island Game!")
print()

print("You are standing at the entrance of an island.")
choice1 = input("Do you want to go LEFT or RIGHT? ").lower()

if choice1 == "left":
    print("\nYou reach a river.")
    choice2 = input("Do you want to SWIM or WAIT? ").lower()

    if choice2 == "wait":
        print("\nA boat arrives and takes you to an island.")
        choice3 = input("Choose a door: RED, BLUE, or GREEN? ").lower()

        if choice3 == "green":
            print("\n🎉 Congratulations!")
            print("💰 You found the TREASURE!")
        elif choice3 == "red":
            print("\n🔥 Oh no! The room is full of fire.")
            print("Game Over!")
        elif choice3 == "blue":
            print("\n🌊 The room is flooded.")
            print("Game Over!")
        else:
            print("\n❌ Invalid choice.")
            print("Game Over!")

    else:
        print("\n🐊 A crocodile attacked you!")
        print("Game Over!")

else:
    print("\n🕳️ You fell into a hole!")
    print("Game Over!")