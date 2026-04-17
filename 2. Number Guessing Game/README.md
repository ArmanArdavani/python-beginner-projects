# Number Guessing Game 🎯

A command-line number guessing game written in Python. The computer picks a random number within a range you define, and you try to guess it before running out of attempts.

## Features

- **Custom number range** — Set your own minimum and maximum values before the game starts
- **Guess limit** — Choose how many attempts you get; the answer is revealed if you run out
- **Best score tracking** — Your fastest win (fewest guesses) is tracked across replays
- **Input validation** — Handles non-numeric input and out-of-range guesses gracefully
- **Replay support** — Play as many rounds as you want without restarting the program

## How to Play

1. Enter a guess limit (e.g., `10`)
2. Enter a minimum and maximum value for the number range (e.g., `1` to `100`)
3. Guess the number — you'll be told if your guess is too high or too low
4. Win by guessing correctly before the limit is reached
5. Choose to play again or exit after each round

## Example

```
Enter the guess limit: 5
Enter the minimum value: 1
Enter the maximum value: 50
Guess the number (between 1 and 50): 25
Too low! Try again.
Guess the number (between 1 and 50): 37
Too high! Try again.
Guess the number (between 1 and 50): 31
Congratulations! You guessed the number in 3 attempts.
Best score: 3 attempt(s).
Do you want to play again? (y/n):
```

## Requirements

- Python 3.x
- No external libraries needed

## How to Run

```bash
python main.py
```

## Project Structure

```
number-guessing-game/
└── main.py
└── README.md
```

## Optional Enhancements Implemented

- [x] Custom min/max number range
- [x] Guess limit with answer reveal on failure
- [x] Best score tracking across multiple rounds

## What I Learned

- Input validation with `try/except`
- Game loop design with nested `while` loops
- Tracking state across multiple rounds with variables
- Extracting repeated logic into helper functions

---

*Part of Mosh Hamedani's Python Projects for Beginners course.*
