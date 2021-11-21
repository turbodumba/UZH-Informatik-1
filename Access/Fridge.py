#!/usr/bin/env python3

class Fridge:

    def __init__(self):
        self.__list = []
        self.__length = 0

    def __iter__(self):
        self.__n = 0
        return self

    def __next__(self):
        if self.__n < self.__length:
            now = self.__n
            self.__n += 1
            return self.__list[now]
        else:
            raise StopIteration

    def __len__(self):
        return self.__length

    def store(self, tup):
        self.__list.append(tup)
        self.__length += 1
        self.__list.sort()

    def find(self, name):
        for i in self.__list:
            if i[1] == name:
                return i
        return None

    def take(self, tup):  # Taking Stuff out of the Fridge
        for i in self.__list:
            if i == tup:
                self.__length -= 1
                self.__list.remove(i)
                return i
        raise Warning("Item not found")

    def take_before(self, date):
        returnlist = []
        removedint = 0
        for i in self.__list:  # find & save
            if i[0] < date:
                returnlist.append(i)
                removedint += 1

        for j in returnlist:  # remove
            self.__list.remove(j)
        self.__length -= removedint
        return returnlist
