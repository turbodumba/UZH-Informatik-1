class Animal:
    def __init__(self, kek):
        self.feet = kek
        self.age = 0
        self.food = 1

    def next_day(self):
        self.age += 1
        self.food -= 1

    def feed(self): self.food += 1

    def is_alive(self): return self.food > 0

    def get_feet(self): return self.feet

    def make_noise(self): pass


cat = Animal(4)
cat.feed()
cat.next_day()
print(cat.is_alive())
print(cat.get_feet())
cat.next_day()
print(cat.is_alive())
