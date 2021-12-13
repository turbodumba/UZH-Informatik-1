#!/usr/bin/env python3
import random


class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        seq = "0123456789ABCDEF"
        retlist = []
        for i in range(self.columns * self.rows):
            new = '0x' + random.choice(seq) + random.choice(seq) + random.choice(seq) + random.choice(seq)
            retlist.append(new)
        return retlist
