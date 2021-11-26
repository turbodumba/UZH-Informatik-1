#!/usr/bin/env python3

from shop import Shop


class ClothingStore(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__clothing_pieces = 0

    def procure(self, price_per_unit, units):
        if units > 10:
            super().procure(price_per_unit * 0.8, units)
        else:
            super().procure(price_per_unit, units)

    def add_procured_units(self, units):
        self.__clothing_pieces += units

    def get_produced_units(self):
        return self.__clothing_pieces

    def set_produced_units(self, units):
        self.__clothing_pieces = units

    def get_status(self):
        lists = list(super().get_status())
        lists.append(self.__clothing_pieces)
        return tuple(lists)
