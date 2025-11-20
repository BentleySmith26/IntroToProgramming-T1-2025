import random

number = random.randint(1, 100)
guesscount = 1
while True:
    try:
        guess = int(input("Please guess the number\n> "))
        if guess > number:
            print("too high")
            guesscount += 1
        elif guess < number:
            print("too little")
            guesscount += 1
        elif guess == number:
            print(f"you got it in {guesscount} guesses!")
            break
    except ValueError:
        print("invalid input")