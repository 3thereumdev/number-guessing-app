import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # You get 10 guesses

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                return  # End the game
        except ValueError:
            print("Please enter a valid number.")

    print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

if __name__ == "__main__":
    play_game()