import random
def guess_game():
    n = random.randint(1,10)
    while True :
        num = int(input("Enter a value:"))
        if n == num :
            print("You Won")
            break
        elif n > num :
            print("Too low")
        else :
            print("To High")
guess_game()