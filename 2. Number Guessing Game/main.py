import random 

# Ask for the guess limit 
while True:
    try:
        guess_limit = int(input('enter the guess limit: '))
    except ValueError:
        print("Please enter a Valid number.")
    else:
        break


# Ask for the minimum value 
while True:
    try:
        min_value = int(input('enter the  minimum value: '))
    except ValueError:
        print("Please enter a Valid number.")
    else:
        break

# Ask for the maximum value 
while True:
    try:
        max_value = int(input('enter the maximum value: '))
    except ValueError:
        print("Please enter a Valid number.")
    else:
        break


# Generate the random number 
random_number = random.randint(min_value, max_value)

number_of_attempts = 0
best_score = None
while True:
    try:
        guess = int(input(f'Guess the number (between {min_value} and {max_value}): '))
        number_of_attempts += 1

        if number_of_attempts == guess_limit:
            print(f"attempt limit reached! the corrent number is {random_number}")
            break

        elif guess not in range(min_value, max_value + 1):
            print("Number out of Range! Try again.")

        elif guess < random_number:
            print("Too low! Try again.")

        elif guess > random_number:
            print("Too high! Try again.")

        elif guess == random_number and best_score is None:
            best_score = number_of_attempts
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")
            print(f"best score: {best_score}")
            number_of_attempts = 0

        elif guess == random_number: 
            if number_of_attempts < best_score:
                best_score = number_of_attempts
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")
            print(f"best score: {best_score}")
            number_of_attempts = 0

            repeat_game = input('do you want to repeat the game? (y/n)').lower()

            if repeat_game == "y":
                pass
            elif repeat_game == "n":
                break
            else:
                print("Please enter 'y' or 'n'")
            
    except ValueError:
        print("Please enter a Valid number.")