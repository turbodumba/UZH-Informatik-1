#!/usr/bin/env python3

from shop import Shop


class Bakery(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__dough = 0
        self.__bread = 0

    def sell(self, price_per_unit, units):
        super().sell(price_per_unit * 0.75, units)

    def produce(self, costs_per_unit):
        if self.__dough * costs_per_unit > self._capital:
            amount_prod = self._capital // costs_per_unit
            self.__bread += amount_prod
            self.__dough -= amount_prod
            self._capital -= amount_prod * costs_per_unit
            raise Warning("Shop low on money")
        self.__bread += self.__dough
        self._capital -= self.__dough * costs_per_unit
        self.__dough = 0

    def add_procured_units(self, units):
        self.__dough += units

    def get_produced_units(self):
        return self.__bread

    def set_produced_units(self, units):
        self.__bread = units

    def pay_rent_and_loan(self, rent):
        amount_owed = super().pay_rent_and_loan(0.8 * rent)
        return amount_owed

    def get_status(self):
        lists = list(super().get_status())
        lists.extend([self.__dough, self.__bread])
        return tuple(lists)
