import sys
class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {}
        self.load_exchange_rates()
    
    def load_exchange_rates(self):
        self.exchange_rates = {
            "USD": 1.0, "EUR": 0.91, "GBP": 0.78, "INR": 83.27,
            "JPY": 151.85, "CNY": 7.22, "AUD": 1.52, "CAD": 1.35,
            "NPR": 132.50, "CHF": 0.89, "SGD": 1.34, "HKD": 7.84,
            "SEK": 10.48, "NZD": 1.67, "KRW": 1320.75, "BRL": 4.98,
            "ZAR": 18.52, "RUB": 92.34, "MXN": 17.20, "IDR": 15950.0,
            "TRY": 32.55, "SAR": 3.75, "AED": 3.67, "THB": 36.50,
            "MYR": 4.69, "PKR": 278.90, "EGP": 30.87, "BDT": 109.50,
            "VND": 24650.0, "PLN": 3.98, "CZK": 23.12, "HUF": 351.47,
            "DKK": 6.84, "ILS": 3.72, "ARS": 880.50, "CLP": 926.15,
            "COP": 3912.75, "PEN": 3.78, "NGN": 1380.45, "KWD": 0.31,
            "BHD": 0.38, "OMR": 0.39, "QAR": 3.64, "LKR": 303.50,
            "MAD": 10.25, "DZD": 136.70, "UAH": 38.75, "BGN": 1.79,
            "RON": 4.92, "KES": 134.25, "TZS": 2550.0, "UGX": 3850.0,
            "GHS": 14.25, "ETB": 56.75, "XAF": 600.50, "XOF": 600.50,
            "MUR": 45.50, "BWP": 14.75, "ZMW": 24.95, "NAD": 18.52,
            "SYP": 2500.0, "IQD": 1310.0, "AFN": 74.75, "MNT": 3450.0,
            "KZT": 458.75, "UZS": 12550.0, "KHR": 4100.0, "MMK": 3200.0,
            "LAK": 19500.0, "YER": 250.00, "SLL": 23000.0, "BND": 1.34,
            "FJD": 2.22, "PGK": 3.57, "TOP": 2.35, "WST": 2.75,
            "VUV": 118.75, "XCD": 2.70, "TTD": 6.80, "JMD": 153.50,
            "BSD": 1.00
        }
    
    def convert(self, from_currency, to_currency, amount):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Invalid currency code!")
        base_amount = amount / self.exchange_rates[from_currency]
        return base_amount * self.exchange_rates[to_currency]

if __name__ == "__main__":
    converter = CurrencyConverter()
    print("Welcome to Currency Converter!")
    
    try:
        from_currency = input("Enter source currency (e.g., USD, EUR, INR): ").strip().upper()
        to_currency = input("Enter target currency (e.g., USD, EUR, INR): ").strip().upper()
        amount = float(input("Enter amount: "))
        
        converted_amount = converter.convert(from_currency, to_currency, amount)
        print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)
    except Exception:
        print("An error occurred. Please try again.")
        sys.exit(1)
