import random

roll_count = 0

while True:
    # Ask to roll
    while True:
        choice = input('Roll the dice? (y/n): ')
        if choice in ("y", "n"):
            break
        else:
            print("Invalid Choice! Enter 'y' or 'n'.")
    
    if choice == "n":
        break
    
    roll_count += 1
    
    # Ask how many dice, with validation
    while True:
        try:
            num_dice = int(input('How many dices do you want to roll? '))
            if num_dice < 1:
                print("Please enter at least 1.")
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Dice Roll logic 
    outcome = [random.randint(1, 6) for i in range(num_dice)]
    print(f"Roll #{roll_count}: {outcome}")
