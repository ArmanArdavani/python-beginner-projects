ALL_RATES = {
    "USD": {"EUR": 0.855, "CAD": 1.366, "GBP": 0.74, "CHF": 0.79, "JPY": 158.70, "AUD": 1.40, "CNY": 6.84},
    "EUR": {"USD": 1.1797, "CAD": 1.606, "GBP": 0.87, "CHF": 0.92, "JPY": 186.03, "AUD": 1.64, "CNY": 8.01},
    "CAD": {"USD": 0.7303 , "EUR": 0.616, "GBP": 0.54, "CHF": 0.57, "JPY": 116.03, "AUD": 1.02, "CNY": 5.00},
    "GBP": {"USD": 1.35, "EUR": 1.15, "CAD": 1.85, "CHF": 1.06, "JPY": 214.46, "AUD": 1.89, "CNY": 9.23},
    "CHF": {"USD": 1.27, "EUR": 1.09, "GBP": 0.94, "CAD": 1.73, "JPY": 202.83, "AUD": 1.78, "CNY": 8.68},
    "JPY": {"USD": 0.0063, "EUR": 0.0054, "GBP": 0.0046, "CAD": 0.0086, "CHF": 0.0049, "AUD": 0.0088, "CNY": 0.043},
    "AUD": {"USD": 0.71, "EUR": 0.61, "GBP": 0.53, "CAD": 0.98, "JPY": 113.39, "CHF": 0.56, "CNY": 4.88},
    "CNY": {"USD": 0.15, "EUR": 0.12, "GBP": 0.11, "CAD": 0.20, "JPY": 23.22, "AUD": 0.20, "CHF": 0.12}
}


CURRENCIES = ["USD", "EUR", "CAD", "GBP", "CHF", "JPY", "AUD", "CNY"]
CURRENCIES_PROMPT= "(USD/EUR/CAD/GBP/CHF/JPY/AUD/CNY)"

def get_inputs():
    while True:
        # Ask for amount
        while True:
            try:
                amount = float(input('Enter the amount: '))
            except ValueError:
                    print("Enter a Valid Number!")
            else:
                break
        
        # Ask for source currency
        while True:
            source_currency = input(f'Source currency {CURRENCIES_PROMPT}: ').upper()
            if source_currency not in (CURRENCIES):
                print("Invalid answer!")
            else:
                break

        # Ask for number of Target Currencies
        while True:
            try:
                number_of_curr = int(input('Enter the number of currencies you want to convert to: '))
            except ValueError:
                print("Enter a Valid Number!")
            else:
                break
            

        # Ask for Target Currency/Currencies
        while True:
            target_currencies = []
            for currency in range(number_of_curr):
                while True:
                    target_currency = input(f'Target currency {CURRENCIES_PROMPT}: ').upper()
                    if target_currency not in (CURRENCIES):
                        print("Invalid answer!")
                        continue
                    elif target_currency in target_currencies:
                        print("Already Selected!")
                        continue
                    else:
                        target_currencies.append(target_currency)
                        break
                    
            break

        return amount, source_currency, target_currencies



def convert(amount, source_currency, target_currencies, conversions):
    for target in target_currencies:
        if source_currency == target:
            conversion = f"{amount} {source_currency} is equal to {amount} {target}"
            print(conversion)
            conversions.append(conversion)
        else:
            rate = ALL_RATES[source_currency][target]
            conversion = f"{amount} {source_currency} is equal to {round(amount * rate, 2)} {target}"  
            print(conversion)
            conversions.append(conversion)


    return conversions



def display_history(conversions):
    print("History of conversions: ")
    for conversion in conversions:
        print(conversion)


def main():
    conversions = []
    while True:
        amount, source_currency, target_currencies = get_inputs ()
        convert(amount, source_currency, target_currencies, conversions)
        repeat = input('Do you want to Convert again? ').lower()
        if repeat != "y":
            display_history(conversions)
            break


if __name__ == "__main__":
    main()
