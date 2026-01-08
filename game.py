import random

print("Welcome to the Number Guessing Game. \nYou have 5 chances to guess the number. Good luck!")

low = int(input("Enter Lower Boundy: "))
high = int(input("Enter High Boundy: "))

print(f"\nYou have 5 chances to guess the correct number between {low} and {high}")

num = random.randint(low, high)
chances = 5
gc = 0

while gc < chances:
    gc += 1
    guess = int(input(f"\nEnter guess number {gc}: "))

    if guess == num:
        print(f"Correct! {guess} was the myster number. \nYou guess it in {gc} attempts.")
        break

    elif gc >= chances and guess != num:
        print(f"Sorry the number was: {num}")
    
    elif guess > num:
        print("Too high. Try again")
    
    elif guess < num:
        print("Too low. Try again")