import random

n = random.randint(1,200)

a = -1
guesses = 0

while a != n:
    a = int(input("Guess the number: "))
    if a > n :
        print("Too high!")
        guesses += 1
    elif a < n:
        print("Too low!")
        guesses += 1

print(f"Congratulations! You guessed the number {n} in {guesses} guesses!")