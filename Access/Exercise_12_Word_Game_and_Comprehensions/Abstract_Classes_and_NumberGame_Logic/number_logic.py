#!/usr/bin/env python3
from game_logic import GameLogic
from random import choice


class NumberLogic(GameLogic):

    def _word_selection(self):
        seq = []
        for i in range(self.num_words):
            new = ''
            while len(new) < self.len_words:
                x = choice('0123456789')
                if x not in new:
                    new += x
            seq.append(new)
        return seq

    def _generate_feedback(self, guess):
        matching = 0
        for i in self.password:
            for j in guess:
                if i == j:
                    matching += 1
        self.num_attempts = self.num_attempts - 1
        return "%d/%d correct" % (matching, self.len_words)

    def check(self, guess):
        if not len(guess) == self.len_words:
            raise Warning("Wrong length")
        for ind, i in enumerate(guess):
            for ind_2, j in enumerate(guess):
                if ind == ind_2:
                    continue
                elif i == j:
                    raise Warning("Guess sequence is wrong")
        return super().check(guess)
