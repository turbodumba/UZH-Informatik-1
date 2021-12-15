from abc import ABC, abstractmethod
import unittest


class Product(ABC):
    def __init__(self, price):
        self._price = price

    @abstractmethod
    def get_price(self):
        pass


class Bottle(Product):
    def __init__(self, price, name):
        super().__init__(price)
        self.name = name

    def get_price(self):
        return self._price


class Crate(Product):
    def __init__(self):
        super().__init__(0)
        self._bottles = []

    def get_size(self):
        return len(self._bottles)

    def add(self, bottle):
        if len(self._bottles) < 20:
            self._bottles.append(bottle)
            self._price += bottle.get_price()
        else:
            raise RuntimeError

    def get_price(self):
        return self._price


class DiscountCrate(Crate):

    def get_price(self):
        if len(self._bottles) > 12:
            return round(self._price * (3 / 4), 2)
        else:
            return round(self._price * (1 - len(self._bottles) * 0.02), 2)


class FixedPriceCrate(Crate):
    def __init__(self, price):
        super().__init__()
        self.fix = price

    def get_price(self):
        return self.fix


class ShopTestSuite(unittest.TestCase):

    def test_crate_add(self):
        c = Crate()
        c.add(Bottle(4.50, "Light Beer"))
        self.assertEqual(c.get_size(), 1)

    def test_crate_max_size(self):
        b = Bottle(1.55, "Bruh")
        d = Crate()
        for i in range(20):
            d.add(b)
        with self.assertRaises(RuntimeError):
            d.add(b)

    def test_crate_price(self):
        f = Crate()
        f.add(Bottle(8.0, "Bri"))
        f.add(Bottle(3.55, "lul"))
        f.add(Bottle(9.45, "lal"))
        self.assertEqual(3, f.get_size())
        self.assertEqual(21, f.get_price())

    def test_discount_crate_price(self):
        l = DiscountCrate()
        l.add(Bottle(8.0, "Bri"))
        l.add(Bottle(3.55, "lul"))
        l.add(Bottle(9.45, "lal"))
        self.assertEqual(3, l.get_size())
        self.assertEqual(19.74, l.get_price())


# DO NOT SUBMIT THE LINES BELOW!
bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")] + 3 * [Bottle(4.00, "Strong Stuff")]
assert (bottles[0].get_price() == 3.50)

c = Crate()
for b in bottles: c.add(b)
assert (c.get_size() == 5)
assert (c.get_price() == 20.00)

c = FixedPriceCrate(11.11)
for b in bottles: c.add(b)

assert (c.get_price() == 11.11)

c = DiscountCrate()
for b in bottles: c.add(b)
assert (c.get_price() == 18.00)
