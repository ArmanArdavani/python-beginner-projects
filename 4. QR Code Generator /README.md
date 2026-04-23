# QR Code Generator

A Python command-line tool that generates one or multiple QR codes from user-provided URLs or text.

## Features

- Generate a single or multiple QR codes in one session
- Each QR code is saved as a `.png` file with a custom filename
- Automatically appends `.png` extension if not provided

## Requirements

- Python 3.x
- `qrcode` library

## Installation

```bash
pip install qrcode[pil]
```

## Usage

```bash
python main.py
```

Follow the prompts to enter URLs/text and filenames. Press **Enter** with no input to stop adding entries and generate all QR codes.

## Example

```
Enter the text or URL for the QR code (or press Enter to stop): https://github.com
Enter the filename for this QR code: github
QR code saved as github.png
```

---

*Part of Mosh Hamedani's Python Projects for Beginners course.*