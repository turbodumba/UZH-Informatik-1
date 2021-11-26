#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar

c = CombustionCar(40.0, 8.0)
print(c.get_remaining_range())  # 500
c.drive(25.0)
print(c.get_gas_tank_status())  # (38.0, 40.0)
try:
    c.drive(1000.0)
except Warning as e:
    print(e)
else:
    raise Warning("Here should have been raised a warning!")

try:
    c.fuel(2.5)
except Warning as e:
    print(e)

e = ElectricCar(25.0, 500.0)
e.drive(100.0)
print(e.get_battery_status())
e.charge(2.0)
print(e.get_battery_status())  # (22.0, 25)
try:
    e.charge(500)
except Warning as e:
    print(e)

h = HybridCar(40.0, 8.0, 25.0, 500.0)
print(h.get_remaining_range())
print(h.get_gas_tank_status())
print(h.get_battery_status())
h.switch_to_combustion()
print(h.get_remaining_range())
h.drive(600.0)  # depletes fuel, auto-switch
print(h.get_gas_tank_status())  # (0.0, 40.0)
print(h.get_battery_status())  # (20.0, 25.0)
