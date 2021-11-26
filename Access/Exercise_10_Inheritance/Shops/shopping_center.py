#!/usr/bin/env python3

class ShoppingCenter:

    def __init__(self, capital, shops):
        self.__capital = capital
        if len(shops) == 0:
            raise Warning("Can't be initialized without a shop")
        self.__shops = tuple(shops)
        self.__debtors = ()
        self.__length = len(shops)

    def collect_rent_and_loan(self, rent):
        to_be_removed = []
        for shop in self.__shops:
            amount = shop.pay_rent_and_loan(rent)
            self.__capital += amount
            if shop in self.__debtors and shop.get_loan() == 0:
                to_be_removed.append(shop)
        for remove in to_be_removed:
            lists = list(self.__debtors)
            lists.remove(remove)
            self.__debtors = tuple(lists)

    def grant_loan(self, shop, interest, amount):
        if shop not in self.__shops:
            raise Warning("This shop isn't in the shopping centre")
        if self.__capital < amount:
            raise Warning("Not enough capital")
        else:
            shop.take_loan(interest, amount)
            self.__capital -= amount
            lists = list(self.__debtors)
            lists.append(shop)
            self.__debtors = tuple(lists)

    def add_shop(self, shop):
        lists = list(self.__shops)
        lists.append(shop)
        self.__shops = tuple(lists)
        self.__length += 1

    def remove_shop(self, shop):
        lists = list(self.__shops)
        if shop in lists:
            ind = lists.index(shop)
            ret = lists[ind]
            lists.remove(shop)
            self.__shops = tuple(lists)
            self.__length -= 1
            return ret

    def get_status(self):
        tup = (self.__capital, self.__shops, self.__debtors)
        return tup

    def __len__(self):
        return self.__length
