import random

EMOJIS = {"r": "🪨", "p": "📃", "s": "✂️"}
WINNING_COMBOS = {"r": "s", "s": "p", "p": "r"}


def display_choice(player_name, choice):
    print(f"{player_name} chose {EMOJIS[choice]}")


def get_player_choice(player_name):
    while True:
        choice = input(f"{player_name} | Rock, paper, scissors? (r/p/s): ").strip().lower()
        if choice in ("r", "p", "s"):
            display_choice(player_name, choice)
            return choice
        print("Invalid choice! Please enter r, p, or s.")


def get_result(choice1, choice2):
    """Returns 1 if player1 wins, 2 if player2 wins, 0 if tie."""
    if choice1 == choice2:
        return 0
    elif WINNING_COMBOS[choice1] == choice2:
        return 1
    else:
        return 2


def print_stats(name1, wins1, losses1, ties1, name2=None, wins2=None, losses2=None, ties2=None):
    print(f"\n{name1} | Wins: {wins1}, Losses: {losses1}, Ties: {ties1}")
    if name2:
        print(f"{name2} | Wins: {wins2}, Losses: {losses2}, Ties: {ties2}")


def play_two_player():
    score1 = score2 = 0
    wins1 = losses1 = ties1 = 0
    wins2 = losses2 = ties2 = 0

    while True:
        choice1 = get_player_choice("Player 1")
        choice2 = get_player_choice("Player 2")

        result = get_result(choice1, choice2)

        if result == 1:
            print("Player 1 wins this round!")
            score1 += 1
            wins1 += 1
            losses2 += 1
        elif result == 2:
            print("Player 2 wins this round!")
            score2 += 1
            wins2 += 1
            losses1 += 1
        else:
            print("It's a tie!")
            ties1 += 1
            ties2 += 1

        if score1 == 2:
            print_stats("Player 1", wins1, losses1, ties1, "Player 2", wins2, losses2, ties2)
            print("🏆 Player 1 is the overall winner!")
            break
        elif score2 == 2:
            print_stats("Player 1", wins1, losses1, ties1, "Player 2", wins2, losses2, ties2)
            print("🏆 Player 2 is the overall winner!")
            break


def play_vs_computer():
    player_score = computer_score = 0
    wins = losses = ties = 0

    while True:
        player_choice = get_player_choice("Player")
        computer_choice = random.choice(["r", "p", "s"])
        display_choice("Computer", computer_choice)

        result = get_result(player_choice, computer_choice)

        if result == 1:
            print("You win this round!")
            player_score += 1
            wins += 1
        elif result == 2:
            print("Computer wins this round!")
            computer_score += 1
            losses += 1
        else:
            print("It's a tie!")
            ties += 1

        if player_score == 2:
            print_stats("You", wins, losses, ties)
            print("🏆 You are the overall winner!")
            break
        elif computer_score == 2:
            print_stats("You", wins, losses, ties)
            print("💻 Computer is the overall winner!")
            break


def main():
    while True:
        game_mode = input("\nTwo player or Play with computer? (two player/computer): ").strip().lower()
        if game_mode in ("two player", "computer"):
            break
        print("Invalid choice! Please enter 'two player' or 'computer'.")

    while True:
        if game_mode == "two player":
            play_two_player()
        else:
            play_vs_computer()

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()