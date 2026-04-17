# 🐍 Python Projects for Beginners

A collection of command-line Python projects built while working through Mosh Hamedani's *Python Projects for Beginners* course. Each project is written from scratch to practice real problem-solving — not just following along.

---

## 🚀 How to Run Any Project

Make sure you have Python 3 installed, then:

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/python-projects.git
cd python-projects

# Run any project
python dice_rolling_game/main.py
```

No external dependencies are needed for most projects. Any that require a library (e.g. QR Code Generator) will say so in that project's own README.

---

## 📁 Project List

| # | Project | Difficulty | Description | Enhancements |
|---|---------|------------|-------------|--------------|
| 01 | [Dice Rolling Game](./dice_rolling_game/) | ⭐⭐ | Simulates rolling a pair of dice, asks to roll again | Roll counter |
| 02 | [Number Guessing Game](./number_guessing_game/) | ⭐⭐⭐ | Computer picks a number, player guesses with hints | Best score tracker |
| 03 | [Rock Paper Scissors](./rock_paper_scissors/) | ⭐⭐⭐ | Classic RPS with emoji output | Win/loss/tie tally |
| 04 | [QR Code Generator](./qr_code_generator/) | ⭐⭐⭐ | Generates a scannable QR code from any URL or text | — |
| 05 | [Currency Converter](./currency_converter/) | ⭐⭐⭐ | Converts between currencies using fixed rates | Conversion history |
| 06 | [Quiz Game](./quiz_game/) | ⭐⭐⭐ | Multiple-choice quiz with score tracking | — |
| 07 | [Tic Tac Toe](./tic_tac_toe/) | ⭐⭐⭐⭐ | Two-player Tic Tac Toe with colored board | Score tracking across rounds |
| 08 | [To-Do List App](./todo_list/) | ⭐⭐⭐⭐ | Add, view, and remove tasks from a list | Save/load from file |
| 09 | [Simple Text Editor](./simple_text_editor/) | ⭐⭐⭐⭐ | Open, edit, and save text files from the terminal | — |
| 10 | [Pig Dice Game](./pig_dice_game/) | ⭐⭐⭐⭐ | Strategic dice game — roll or hold to reach 100 points | Custom target score |
| 11 | [Cows and Bulls](./cows_and_bulls/) | ⭐⭐⭐⭐ | Guess a 4-digit number with positional feedback | — |
| 12 | [Password Strength Checker](./password_strength_checker/) | ⭐⭐⭐⭐ | Rates password strength across 5 levels | Improvement suggestions |
| 13 | [Password Generator](./password_generator/) | ⭐⭐⭐⭐⭐ | Generates secure passwords based on user criteria | Save to file |
| 14 | [Word Guessing Game](./word_guessing_game/) | ⭐⭐⭐⭐⭐ | Guess a random word letter by letter (like Hangman) | Win/loss session record |
| 15 | [Slot Machine Game](./slot_machine_game/) | ⭐⭐⭐⭐⭐ | Bet and spin — matches pay out at different rates | — |
| 16 | [ATM Simulation](./atm_simulation/) | ⭐⭐⭐⭐⭐⭐ | Full ATM system using OOP — balance, deposit, withdraw | PIN system, transaction history |

---

## 🧠 What I Learned

Working through these projects taught me:

- Core Python: loops, conditionals, functions, and data structures
- Working with files (reading, writing, appending)
- Using the `random` module for games and simulations
- Input validation and basic error handling
- Basic Object-Oriented Programming (classes and methods) in the ATM project
- How to structure a project folder and write clean, readable code

---

## 📂 Repo Structure

```
python-projects/
├── README.md                   ← You are here
├── .gitignore
├── dice_rolling_game/
│   ├── main.py
│   └── README.md
├── number_guessing_game/
│   ├── main.py
│   └── README.md
└── ... (same pattern for each project)
```

---

## 🛠️ Built With

- Python 3
- Standard library only (except `qrcode` library for the QR Code Generator)

---

## 📌 Status

![Status](https://img.shields.io/badge/status-in%20progress-yellow)

Currently working through the project list. Completed projects are linked above.

---

*Course by [Mosh Hamedani](https://codewithmosh.com) — projects written independently as practice.*