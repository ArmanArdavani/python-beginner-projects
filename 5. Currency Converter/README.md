# Currency Converter
A Python command-line tool that converts an amount from one currency to one or multiple currencies using fixed exchange rates.

## Features
- Convert an amount to multiple target currencies at once
- Supports 8 major currencies: USD, EUR, CAD, GBP, CHF, JPY, AUD, CNY
- Prevents duplicate target currency selection
- Case-insensitive currency input
- Keeps a history of all conversions made during the session, displayed on exit

## Requirements
- Python 3.x

## Installation
No external libraries required.

## Usage
```bash
python main.py
```
Follow the prompts to enter an amount, source currency, and one or more target currencies. Enter `n` when asked to convert again to exit and view your conversion history.

## Example
```
Enter the amount: 100
Source currency (USD/EUR/CAD/GBP/CHF/JPY/AUD/CNY): USD
Enter the number of currencies you want to convert to: 2
Target currency (USD/EUR/CAD/GBP/CHF/JPY/AUD/CNY): EUR
Target currency (USD/EUR/CAD/GBP/CHF/JPY/AUD/CNY): JPY
100.0 USD is equal to 85.5 EUR
100.0 USD is equal to 15870.0 JPY
Do you want to Convert again? n

History of conversions:
100.0 USD is equal to 85.5 EUR
100.0 USD is equal to 15870.0 JPY
```

---
*Part of Mosh Hamedani's Python Projects for Beginners course.*