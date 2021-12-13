#!/usr/bin/env python3
from game_logic import GameLogic
from random import shuffle


# This is the current version of WordLogic that needs to be adapted
class WordLogic(GameLogic):

    def _word_selection(self):
        words = self.__find_words_with_right_size()
        shuffle(words)
        return words[0:self.num_words]

    def __find_words_with_right_size(self):
        with open("words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def check(self, guess):
        super().check(guess)

    def _generate_feedback(self, guess):
        matching = 0
        for i in range(self.len_words):
            if guess[i] == self.password[i]: matching += 1
        self.num_attempts = self.num_attempts - 1
        return "%d/%d correct" % (matching, self.len_words)
