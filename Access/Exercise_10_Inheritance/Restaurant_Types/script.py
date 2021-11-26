#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from onsite_restaurant import OnsiteRestaurant
from delivery_restaurant import DeliveryRestaurant
from restaurant import Restaurant

restaurant_one = Restaurant('Restaurant One', "Mixed Cuisine")
restaurant_one.add_consumption_unit("Caesar Salad", 15)
restaurant_one.open_restaurant()
restaurant_one.sell_unit("Caesar Salad")
restaurant_one.sell_unit("Caesar Salad")
restaurant_one.sell_unit("Caesar Salad")
print(restaurant_one.get_sales())  # 3 * 15

onsite_one = OnsiteRestaurant("Onsite Steak One", "Steaks", 3, True)
print(onsite_one.get_available_tables())
onsite_one.occupy_table()
onsite_one.occupy_table()
onsite_one.occupy_table()
print(onsite_one.get_available_tables())
try:
    onsite_one.occupy_table()
except Warning as e:
    print(e)

print(onsite_one.get_available_tables())
onsite_one.free_table()
onsite_one.free_table()
onsite_one.free_table()
print(onsite_one.get_available_tables())
try:
    onsite_one.free_table()
except Warning as e:
    print(e)

print(onsite_one.get_available_tables())
msg = onsite_one.describe_restaurant()
print(msg)

deli_one = DeliveryRestaurant("Kebab Delivery One", "Kebab", 20)
print(deli_one.is_in_range(10))
print(deli_one.is_in_range(20))
print(deli_one.is_in_range(21))
deli_one.add_consumption_unit("Kebab", 11)
deli_one.add_consumption_unit("Fries", 5)
deli_one.add_consumption_unit("Dönerbox", 10)
try:
    deli_one.sell_unit('Fries')
except Warning as e:
    print(e)
deli_one.open_restaurant()
deli_one.sell_unit('Kebab')
deli_one.sell_unit('Fries')
deli_one.sell_unit('Dönerbox')
print(deli_one.get_sales())
menu = deli_one.get_menu()
print(deli_one.get_menu())
menu.clear()
print(menu)
print(deli_one.get_menu())
deli_one.remove_consumption_unit('Fries')
print(deli_one.get_menu())