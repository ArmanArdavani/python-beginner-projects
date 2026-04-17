import random

roll_count = 0
while True:
    # Ask for the dice roll
    while True:
        choice = input('Roll the dice? (y/n): ')
        if choice in ("y", "n"):
            break
        else:
            print("Invalid Choice! Enter 'y' or 'n'.")
    
    if choice == "y":
        roll_count += 1
    else:
        break
    
    # Ask for number of dices, validate/handle ValueError and print the outcome
    while True:
        try:
            number_of_dices = int(input('How many dices do you want to roll? '))
            list_of_outcomes = []
            for i in range(number_of_dices):
                dice_outcome = random.randint(1,6)
                list_of_outcomes.append(dice_outcome)

            print(f"Roll Count: {roll_count}")
            print(list_of_outcomes)
            break
    
        except ValueError:
            print("Enter a Valid integer.")






    

    
