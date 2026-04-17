# Dice Rolling Game 🎲

A command-line dice rolling simulator written in Python. Roll as many dice as you want, track how many times you've rolled, and keep playing until you're done.

## Features

- **Custom dice count** — Choose how many dice to roll each turn
- **Roll counter** — Tracks how many times you've rolled during the session
- **Input validation** — Handles non-numeric input and invalid choices gracefully
- **Replay support** — Keep rolling or quit whenever you want

## How to Play

1. When prompted, enter `y` to roll or `n` to quit
2. Enter how many dice you want to roll (e.g., `2`)
3. See the result of each die displayed instantly
4. Your total roll count is shown after every roll
5. Enter `n` at any point to end the session

## Example

```
Roll the dice? (y/n): y
How many dice do you want to roll? 3
Roll #1: [4, 2, 6]
Roll the dice? (y/n): y
How many dice do you want to roll? 2
Roll #2: [1, 5]
Roll the dice? (y/n): n
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
dice-rolling-game/
└── main.py
└── README.md
```

## Optional Enhancements Implemented

- [x] Custom dice count per roll
- [x] Roll counter tracking across the session

## What I Learned

- Input validation with `try/except`
- Game loop design with nested `while` loops
- List comprehensions for generating dice outcomes
- Tracking state across multiple rolls with a counter variable

---

*Part of Mosh Hamedani's Python Projects for Beginners course.*