import time
import random
import sys
maxnumber = 10
guess = 0
lives = 0
diff = "none"
score = 0
level = 0


def leveltypes():
    global level, lives, diff
    if level == 1:
        diff = "easy"
        lives = 10
    elif level == 2:
        diff = "medium"
        lives = 5
    elif level == 3:
        diff = "hard"
        lives = 3



def start():
    print("welcome to the guessing game :3")
    time.sleep(.5)
    print("you will have to guess the number in an amount of tries!")
    difficulty()


def difficulty():
    global level
    print("select the difficulty :3")
    time.sleep(.5)
    print("1. easy (10 chances)")
    print("2. medium (5 chances)")
    print("3. hard (3 chances)")
    while True:
        try:
            level = int(input("enter difficulty (1/2/3): "))
            if level < 1 or level > 3:
                print("invalid difficulty")
                continue
            else:
                leveltypes()
                startgame()
                break
        except ValueError:
            print("wrong difficulty\n")


def correctnumber():
    global score, maxnumber
    score += 1
    print("you got the number!")
    time.sleep(.5)
    print(f"your score is {score}")
    if score % 4 == 0:
        maxnumber += 10

    while True:
        choice = input("would you like to play again? (y/n): ").lower()
        if choice == "y":
            again = input("would you like to change the difficulty? (y/n): ").lower()
            if again == "y":
                difficulty()
            else:
                leveltypes()
                startgame()
            break
        elif choice == "n":
            print("thanks for playing!")
            sys.exit()
        else:
            print("please enter y or n")


def startgame():
    global guess, lives
    print(f"\nyou have chosen difficulty: {diff}")
    time.sleep(.5)
    print(f"you will have to guess a number from 1 to {maxnumber}")
    time.sleep(.5)
    print(f"you have {lives} guesses left")
    guess = random.randint(1, maxnumber)
    print(guess)

    while lives > 0:
        try:
            enternum = int(input("enter your guess: "))
            if enternum == guess:
                correctnumber()
                break
            elif enternum < guess:
                print("your guess is too low")
            else:
                print("your guess is too high")
            lives -= 1
            if lives > 0:
                print(f"you have {lives} guesses left")
            else:
                print(f"you ran out of lives! the number was {guess}")
        except ValueError:
            print("enter a number")

if __name__ == "__main__":
    start()
