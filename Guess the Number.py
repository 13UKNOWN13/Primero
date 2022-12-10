import random

def guess(x):
   random_number = random.randint(1, x)
   guess = 0
   while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        elif guess == random_number:
            str(random_number)
            print(f"Yay, You have guessed the correct number " + str(random_number) + " correctly!")
guess(20)
# Make it to where the user can choose the minimum and maximum number they want to guess.
# Have a solution for if someone inputs words instead of numbers