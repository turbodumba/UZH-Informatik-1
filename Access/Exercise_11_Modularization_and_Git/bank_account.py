#!/usr/bin/env python3
# add imports, if necessary
from currency_converter import convert
from exchange_rates import EXCHANGE_RATES


class BankAccount:

    def __init__(self, currency="CHF"):
        self.__balance = 0
        if currency not in EXCHANGE_RATES:
            raise Warning("Invalid currency")
        self.__currency = currency

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance

    def deposit(self, amount, currency="CHF"):
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise Warning("The given Amount is not a number")
        if amount < 0 or currency not in EXCHANGE_RATES:
            raise Warning("Invalid amount or exchange rates not available")
        if currency == self.get_currency():
            self.__balance += amount
        else:
            conv_amount = convert(amount, currency, self.__currency)
            self.__balance += conv_amount

    def withdraw(self, amount, currency="CHF"):
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise Warning("The given Amount is not a number")
        if amount < 0 or currency not in EXCHANGE_RATES:
            raise Warning("Invalid amount or exchange rates not available")
        if currency == self.get_currency():
            if self.__balance - amount < 0:
                raise Warning("Can't withdraw what you don't have... aka you are broke af")
            self.__balance -= amount
        else:
            conv_amount = convert(amount, currency, self.__currency)
            if self.__balance - conv_amount < 0:
                raise Warning("Can't withdraw what you don't have... aka you are broke af")
            self.__balance -= conv_amount
