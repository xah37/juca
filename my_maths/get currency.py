
# https://v6.exchangerate-api.com/v6/8f31ee39070def5ab217093a/latest/USD
import requests


class RealTimeCurrencyConvertor():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount/self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount


url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConvertor(url)
print(converter.convert('USD', 'SLL', 100))
