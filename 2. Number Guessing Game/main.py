import random 

def get_integer_input (prompt, min_val = None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a number of at least {min_val}")
            else:
                return value
        except ValueError:
            print("Please enter a Valid number.")

# Setup
guess_limit = get_integer_input('Enter the guess limit: ', min_val=1)
min_value = get_integer_input('Enter the minimum value: ')
 

while True:
    max_value = get_integer_input('Enter the maximum value: ')
    if max_value > min_value:
        break
    print(f"Maximum value should be greater than minimum value ({min_value})")


# Game loop
best_score = None

while True:
    # Generate the random number 
    random_number = random.randint(min_value, max_value)
    number_of_attempts = 0

    while True:
        try:
            guess = int(input(f'Guess the number (between {min_value} and {max_value}): '))
            number_of_attempts += 1

            if guess not in range(min_value, max_value + 1):
                print("Number out of Range! Try again.")
                number_of_attempts -= 1   # Don't penalize for invalid range input

            elif guess < random_number:
                print("Too low! Try again.")
                if number_of_attempts == guess_limit:
                    print(f"Attempt limit reached! The correct number was {random_number}.")
                    break

            elif guess > random_number:
                print("Too high! Try again.")
                if number_of_attempts == guess_limit:
                    print(f"Attempt limit reached! The correct number was {random_number}.")
                    break

            else: #correct guess 
                if best_score is None or number_of_attempts < best_score:
                    best_score = number_of_attempts
                print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")
                print(f"Best score: {best_score} attempt(s).")
                break

        except ValueError:
            print("Please enter a Valid number.")
    
    repeat_game = input('Do you want to play again? (y/n): ').lower()
    while repeat_game not in ("y", "n"):
        print("Please enter 'y' or 'n'. ")
        repeat_game = input('Do you want to play again? (y/n): ').lower()

    if repeat_game == "n":
        print("Thanks for playing! Goodbye.")
        break
