import random

number = random.randint(1, 10)

guess = int(input("Enter your guess: "))

while guess != number:
    print("Wrong guess")
    guess = int(input("Enter your guess: "))
    if guess == -1:
        print("You quit the game")
        exit()

print("You guessed the number! It was", number)



