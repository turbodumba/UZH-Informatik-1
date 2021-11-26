#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        if not (type(gas_capacity) == float and type(gas_per_100km) == float and type(battery_size) == float and type(
                battery_range_km) == float):
            raise Warning("Invalid type")
        if gas_capacity < 0 or gas_per_100km < 0 or battery_size < 0 or battery_range_km < 0:
            raise Warning("Negative amount")
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__current_mode = 'ele'

    def switch_to_combustion(self):
        self.__current_mode = 'com'

    def switch_to_electric(self):
        self.__current_mode = 'ele'

    def get_remaining_range(self):
        return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)

    def drive(self, dist):
        if not type(dist) == float or dist < 0:
            raise Warning("Invalid type or negative amount")
        if self.__current_mode == 'ele':
            try:
                pos_rng = ElectricCar.get_remaining_range(self)
                ElectricCar.drive(self, dist)
            except Warning:
                self.switch_to_combustion()
                if CombustionCar.get_remaining_range(self) > 0:
                    try:
                        CombustionCar.drive(self, dist - pos_rng)
                    except Warning:
                        raise Warning("Gas tank and battery are both empty")
                else:
                    raise Warning("Gas tank and battery are both empty")
        else:
            try:
                pos_rng = CombustionCar.get_remaining_range(self)
                CombustionCar.drive(self, dist)
            except Warning:
                self.switch_to_electric()
                if ElectricCar.get_remaining_range(self) > 0:
                    try:
                        ElectricCar.drive(self, dist - pos_rng)
                    except Warning:
                        raise Warning("Gas tank and battery are both empty")
                else:
                    raise Warning("Gas tank and battery are both empty")
