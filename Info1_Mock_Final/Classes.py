import random


class Person:
    def __init__(self, name=None, sex=random.choice('fm')):
        self.name = name
        self.sex = sex
        self.offspring = []

    def mate_with(self, other):
        if self.sex == other.sex:
            raise ValueError
        offspring = Person()
        self.offspring.append(offspring)
        other.offspring.append(offspring)
        return offspring

    def __str__(self):
        if len(self.offspring) == 0:
            return self.name + ' (' + self.sex + ') has no children'
        elif len(self.offspring) == 1:
            return self.name + ' (' + self.sex + ') has 1 child: ' + self.offspring[0].name
        else:
            string = self.name + ' (' + self.sex + ') has ' + str(len(self.offspring)) + ' children: '
            for kid in self.offspring:
                if kid == self.offspring[-1]:
                    string += kid.name
                else:
                    string += kid.name + ', '
            return string

    def __repr__(self):
        return self.__str__()


# DO NOT SUBMIT THE LINES BELOW!
p1 = Person("Mark", "m")
p2 = Person("Betty", "f")
p3 = Person("John", "m")
p4 = Person("Anna", "f")
child = p1.mate_with(p2)
assert (child.name == None)
child.name = "Andrea"
assert (len(p1.offspring) == 1)
child = p3.mate_with(p2)
assert (len(p2.offspring) == 2)
child.name = "Terry"
assert (p1.__str__() == "Mark (m) has 1 child: Andrea")
assert (p2.__str__() == "Betty (f) has 2 children: Andrea, Terry")
assert (p3.__repr__() == "John (m) has 1 child: Terry")
assert (p4.__repr__() == "Anna (f) has no children")
