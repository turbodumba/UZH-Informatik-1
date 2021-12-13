#!/usr/bin/env python3

import random
from difflib import SequenceMatcher
from math import floor


class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def word_selection(self):
        words = self.find_words_with_right_size()
        random.shuffle(words)

        # TODO: instead of returning a random sample of words, use the strategy described in task 2
        ret_list = []
        for i in range(floor(self.num_words / 3)):
            ret_list.append(words.pop(words.index(random.choice(words))))
        while len(ret_list) < self.num_words:
            rand_1 = random.choice(ret_list)
            rand_2 = random.choice(words)
            if rand_1 == rand_2:
                continue
            else:
                if self.is_similar(rand_1, rand_2, 0.4):
                    ret_list.append(rand_2)
                    words.remove(rand_2)
        return ret_list

    def is_similar(self, a, b, threshold):
        if threshold < SequenceMatcher(None, a, b).ratio():
            return True
        return False
