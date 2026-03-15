print("Welcome to the Forest Adventure!")
print("You are lost in a dark forest.")
print("You see two paths.")
choice = input("Do you want to go left or right:").lower()
if choice == "left":
    print("You find a river:")
    action = input("Do you swim or walk along the river? ").lower()
    if action == "swim":
        print("Oh no! The current is too strong.")
        print("Game Over 💀!")
    else:
        print("You follow the river and find a village.")
        print("You Win 🏆!")

elif choice == "right":
    print("You meet a hungry tiger!")
    action = input("Do you run or climb a tree? ").lower()

    if action == "climb":
        print("The tiger cannot reach you.")
        print("You survive and win 🏆!")
    else:
        print("The tiger catches you.")
        print("Game Over 💀!")

else:
    print("You got lost in the forest.")
    print("Game Over!")