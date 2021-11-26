#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car


class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if not (type(gas_capacity) == float and type(gas_per_100km) == float):
            raise Warning("Invalid type")
        if gas_capacity < 0 or gas_per_100km < 0:
            raise Warning("Negative amount")
        self.__gas_capacity = gas_capacity
        self.__gas = gas_capacity
        self.__gas_per_100km = gas_per_100km

    def fuel(self, f):
        if not type(f) == float or f < 0:
            raise Warning("Invalid type or negative amount")
        if self.__gas + f > self.__gas_capacity:
            raise Warning("The gas tank was overfilled")
        self.__gas += f

    def get_gas_tank_status(self):
        tup = (self.__gas, self.__gas_capacity)
        return tup

    def get_remaining_range(self):
        return self.__gas / self.__gas_per_100km * 100

    def drive(self, dist):
        if not type(dist) == float or dist < 0:
            raise Warning("Invalid type or negative amount")
        if dist >= self.__gas / self.__gas_per_100km * 100:
            self.__gas = 0
            raise Warning("The gas tank is empty")
        minus_gas = self.__gas_per_100km * dist / 100
        self.__gas -= minus_gas
