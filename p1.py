import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Variable to track the number of guesses
    attempts = 0
    
    while True:
        # Get the user's guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1
        
        # Check if the guess is too low, too high, or correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Start the game
guess_the_number()
