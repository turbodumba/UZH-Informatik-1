#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car


class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if not (type(battery_size) == float and type(battery_range_km) == float):
            raise Warning("Invalid type")
        if battery_size < 0 or battery_range_km < 0:
            raise Warning("Negative amount")
        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km
        self.__bat_charge = battery_size

    def charge(self, kwh):
        if not type(kwh) == float or kwh < 0:
            raise Warning("Invalid type or negative amount")
        if self.__bat_charge + kwh > self.__battery_size:
            raise Warning("The battery was being overcharged")
        self.__bat_charge += kwh

    def get_battery_status(self):
        tup = (self.__bat_charge, self.__battery_size)
        return tup

    def get_remaining_range(self):
        return self.__bat_charge / self.__battery_size * self.__battery_range_km

    def drive(self, dist):
        if not type(dist) == float or dist < 0:
            raise Warning("Invalid type or negative amount")
        if dist >= self.__bat_charge / self.__battery_size * self.__battery_range_km:
            self.__bat_charge = 0
            raise Warning("The battery has no charge left")
        minus_charge = dist / self.__battery_range_km * self.__battery_size
        self.__bat_charge -= minus_charge
