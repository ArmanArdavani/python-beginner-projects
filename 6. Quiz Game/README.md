# Quiz Game

A Python command-line quiz game where the player answers multiple-choice questions from a chosen category and receives a final score.

## Features

- Choose from 4 categories: General Knowledge, Science, History, and Technology
- Multiple-choice questions with 4 options each
- Input validation for both category selection and answer input
- Displays correct/wrong feedback after each question
- Shows final score at the end of the quiz
- Questions loaded from an external `questions.json` file for easy updates

## Requirements

- Python 3.x

## Installation

No external libraries required.

## Usage

```bash
python main.py
```

Follow the prompts to select a category and answer each question by entering `a`, `b`, `c`, or `d`.

## Example

```
What category? General Knowledge/Science/History/Technology: Science
1. What planet is known as the Red Planet?
a) Venus
b) Jupiter
c) Saturn
d) Mars
Enter the answer: d
Your answer: d
Correct!

2. What gas do plants absorb from the atmosphere?
a) Oxygen
b) Nitrogen
c) Carbon Dioxide
d) Hydrogen
Enter the answer: c
Your answer: c
Correct!

Your final score: 2/2
```

---

*Part of Mosh Hamedani's Python Projects for Beginners course.*