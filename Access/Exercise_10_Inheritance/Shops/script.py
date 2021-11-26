#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from bakery import Bakery
from clothing_store import ClothingStore
from shopping_center import ShoppingCenter

bakery = Bakery(1000)  # (capital, loan, interest, initial_loan_amount, dough, bread) = (1000, 0, 0, 0, 0, 0)
bakery.take_loan(0.1, 1000)  # (2000, 1000, 0.1, 1000, 0, 0)
amount_paid_b = bakery.pay_rent_and_loan(100)  # (1720.0, 900, 0.1, 1000, 0, 0)
print(amount_paid_b)
print(bakery.get_status())
bakery.procure(1, 100)  # (1620.0, 900, 0.1, 1000, 100, 0)
print(bakery.get_status())
bakery.produce(1)  # (1520.0, 900, 0.1, 1000, 0, 100)
print(bakery.get_status())
bakery.sell(6, 50)  # (1745.0, 900, 0.1, 1000, 0, 50)
print(bakery.get_status())
bakery.procure(1, 500)
print(bakery.get_status())

try:
    bakery.take_loan(0.1, 1000)
except Warning:
    print("Bakery already has a loan")
else:
    raise Warning("Here should have been raised a warning!")

clothing_store = ClothingStore(
    2000)  # (capital, loan, interest, initial_loan_amount, clothing_pieces) = (2000, 0, 0, 0, 0)
clothing_store.take_loan(0.1, 1000)  # (3000, 1000, 0.1, 1000, 0)
print(clothing_store.get_status())
amount_paid_c = clothing_store.pay_rent_and_loan(100)  # (2700.0, 900, 0.1, 1000, 0)
print(amount_paid_c)
print(clothing_store.get_status())
clothing_store.procure(1, 100)  # (2620.0, 900, 0.1, 1000, 100)
print(clothing_store.get_status())
clothing_store.sell(10, 10)  # (2720.0, 900, 0.1, 1000, 90)
print(clothing_store.get_status())

bakery_two = Bakery(90000)
shopping_center = ShoppingCenter(10000, [bakery_two])  # capital = 10000
print(len(shopping_center))
clot = ClothingStore(200000)
shopping_center.add_shop(clot)  # capital = 10000
print(len(shopping_center))
print(shopping_center.get_status())
shopping_center.grant_loan(bakery_two, 0.05, 100)  # capital = 9000
shopping_center.grant_loan(clot, 1, 500)
print(shopping_center.get_status())
print(bakery_two.get_loan())
shopping_center.collect_rent_and_loan(100)
shopping_center.collect_rent_and_loan(100)  # capital = 9330
shopping_center.collect_rent_and_loan(100)
bak = Bakery(69000)
shopping_center.add_shop(bak)
shopping_center.grant_loan(bak, 0.5, 500)
shopping_center.collect_rent_and_loan(100)
shopping_center.collect_rent_and_loan(100)
shopping_center.collect_rent_and_loan(100)
shopping_center.collect_rent_and_loan(100)
shopping_center.collect_rent_and_loan(100)
shopping_center.collect_rent_and_loan(100)
print(shopping_center.get_status())
shopping_center.collect_rent_and_loan(100)
print(shopping_center.get_status())
print(bakery_two.get_loan())

try:
    shopping_center2 = ShoppingCenter(69, [])
except Warning as e:
    print(e)
else:
    print("not working")

shopping_center.remove_shop(bak)