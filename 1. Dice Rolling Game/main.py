import random

number_of_dices = int(input("how many dices do you want to roll? "))
roll_counter = 1

def roll_dice(number_of_dices):
    global roll_counter
    list = []
    for  roll in range(number_of_dices):
        list.append(random.randint(1,6))
    print(list)
    print(f"roll count: {roll_counter}")
    repeat = input("Roll the dice? (y/n): ").lower()
    if repeat == "y":
        roll_counter += 1 
        roll_dice(number_of_dices)
    elif repeat == "n":
        print("Thanks For Playing")
    else:
        print("Invalid Choice!")        
roll_dice(number_of_dices)



    

    
