# Number Guessing Game
import random

def guessing_game():
    print("Number Guessing Game")
    print("I'm thinking of a number between 1 and 50")
    
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempts!")
            return
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        print(f"Attempts left: {max_attempts - attempts}")
    
    print(f"Game over! The number was {secret_number}")

guessing_game()
