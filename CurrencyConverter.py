import sys
class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {}
        self.load_exchange_rates()
   