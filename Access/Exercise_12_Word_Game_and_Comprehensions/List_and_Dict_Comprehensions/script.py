#!/usr/bin/python3
import string

from data import words


def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]


def words_containing_string(s):
    return [word for word in words if s in word]


def words_starting_with_character(c):
    return [word for word in words if word.startswith(c)]


def alphabet():
    '''you don't have to solve this one using a comprehension.'''
    return string.ascii_lowercase


def dictionary():
    return {x: words_starting_with_character(x) for x in alphabet()}


def censored_words(s):
    return [word if s not in word else len(word)*'x' for word in words]
