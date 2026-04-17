import random

computer_score = 0

user1_score = 0
user1_wins = 0
user1_loses = 0
user1_ties = 0

user2_score = 0
user2_wins = 0
user2_loses = 0
user2_ties = 0

EMOJIS = {"r": "🪨" , "p": "📃", "s": "✂️"}

def display_choice(player_name, choice):
    print(f"{player_name} chose {EMOJIS[choice]}")

# Ask for Two player mode or computer mode and Validate 
while True:
    game_mode = input('Two player or Play with computer? (two player/computer) ').lower()
    if game_mode in ("two player", "computer"):
        break
    else:
        print("Invalid Choice! please enter 'two player' or 'computer ")

while True:
    while True:
        # Get player 1 choice and Validate 
        user1_choice = input('Player 1 | Rock, paper, scissors? (r/p/s): ')
        if user1_choice in ("r", "p", "s"):
            display_choice("Player 1", user1_choice) 
            break
        else:
            print("Invalid Choice!")
         
        

    # <<<Two player mode>>>
    # Get player 2 choice and Validate
    if game_mode == "two player":
        while True:
            user2_choice = input('player 2 | Rock, paper, scissors? (r/p/s): ')
            if user2_choice in ("r", "p", "s"):
                display_choice("Player 2", user2_choice)
                break
            else:
                print("Invalid choice!")

        # Logic of winning and losing 
        if user1_choice == "r":
            if user2_choice == "p":
                print("Player 2 Won")
                user2_score += 1
                user1_loses += 1 
                user2_wins += 1
            elif user2_choice == "s":
                print("Player 1 Won")
                user1_score += 1
                user1_wins += 1 
                user2_loses += 1
            else:
                print("Draw")
                user1_ties += 1
                user2_ties += 1
        
        elif user1_choice == "p":
            if user2_choice == "r":
                print("Player 1 Won")
                user1_score += 1
                user1_wins += 1 
                user2_loses += 1
            elif user2_choice == "s":
                print("Player 2 Won")
                user2_score += 1
                user1_loses += 1 
                user2_wins += 1
            else:
                print("Draw")
                user1_ties += 1
                user2_ties += 1
        
        elif user1_choice == "s":
            if user2_choice == "r":
                print("Player 2 Won")
                user2_score += 1
                user1_loses += 1 
                user2_wins += 1
            elif user2_choice == "p":
                print("Player 1 Won")
                user1_score += 1
                user1_wins += 1 
                user2_loses += 1
            else:
                print("Draw")
                user1_ties += 1
                user2_ties += 1
            
        # logic of whoever ones 2/3 games wins + tally of user wins, loses and ties
        if user1_score == 2:
            print(f"Player 1 | Wins: {user1_wins}, Losses: {user1_loses}, Ties: {user1_ties}")
            print(f"Player 2 | Wins: {user2_wins}, Losses: {user2_loses}, Ties: {user2_ties}")
            print("Player 1 is the winner!")
            break

        elif user2_score == 2:
            print(f"Player 1 | Wins: {user1_wins}, Losses: {user1_loses}, Ties: {user1_ties}")
            print(f"Player 2 | Wins: {user2_wins}, Losses: {user2_loses}, Ties: {user2_ties}")
            print("Player 2 is the winner!")
            break
            


    # <<<Computer mode>>>
    elif game_mode == "computer":
        # Generate computers random choice
        list_of_options = ['r', 'p', 's'] 
        computer_choice = random.choice(list_of_options)
        display_choice("Computer", computer_choice)

        # Logic of winning and losing 
        if user1_choice == "r":
            if computer_choice == "p":
                print("You lose")
                computer_score += 1
                user1_loses += 1 
            elif computer_choice == "s":
                print("You win")
                user1_score += 1
                user1_wins += 1 
            else:
                print("Draw")
                user1_ties += 1

        elif user1_choice == "p":
            if computer_choice == "r":
                print("You win")
                user1_score += 1
                user1_wins += 1
            elif computer_choice == "s":
                print("You lose")
                computer_score += 1 
                user1_loses += 1
            else:
                print("Draw")
                user1_ties += 1

        elif user1_choice == "s":
            if computer_choice == "r":
                print("You lose")
                computer_score += 1
                user1_loses += 1 
            elif computer_choice == "p":
                print("You win")
                user1_score += 1
                user1_wins += 1
            else:
                print("Draw")
                user1_ties += 1

        # logic of whoever ones 2/3 games wins + tally of user wins, loses and ties
        if user1_score == 2:
            print(f"Wins: {user1_wins}")
            print(f"Losses: {user1_loses}")
            print(f"Ties: {user1_ties}")
            print("You are the winner!")
            break

        elif computer_score == 2:
            print(f"Wins: {user1_wins}")
            print(f"Losses: {user1_loses}")
            print(f"Ties: {user1_ties}")
            print("Computer is the winner!")
            break
    else:
        print("Game mode Invalid! (two player/computer) ")
        break

    user_continue = input("Continue? (y/n) ").strip().lower()
    if user_continue != "y":
        break