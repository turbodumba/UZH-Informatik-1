import random


class Dog:
    def __init__(self, name, breed, age, sex):
        self.name = name
        self.breed = breed
        self.age = age
        self.sex = sex
        self.tricks = {}

    def __add__(self, other):
        if not self.sex == other.sex:
            if not self.age < 1 and not other.age < 1:
                gen_num = random.randint(0, 1)
                if gen_num == 1:
                    gend = 'male'
                else:
                    gend = 'female'
                if self.breed == other.breed:
                    return Dog(None, self.breed, 0, gend)
                else:
                    return Dog(None, 'Mutt', 0, gend)

    def learn_trick(self, t):
        liste = list(self.tricks)
        liste.append(t)
        self.tricks = set(liste)
