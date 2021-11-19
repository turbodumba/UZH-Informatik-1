#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        lower_list = []
        keywords = sorted(keywords, reverse=True, key=len)
        print(keywords)
        for i in keywords:
            lower_list.append(i.lower())
        self.__keywords = lower_list
        self.__replacement = template

    def filter(self, msg):
        split_msg = msg.split()
        filtered_string = ""
        first = True
        for word in split_msg:
            for keyword in self.__keywords:
                index = word.lower().find(keyword)
                if index != -1:
                    repl_str = self.__clean(keyword)
                    word = word[0:index] + repl_str + word[index + len(keyword):]
                else:
                    continue
            if first:
                filtered_string += word
                first = False
            else:
                filtered_string += " " + word
        return filtered_string

    def __clean(self, word):
        replacement_string = ""
        length = len(word)
        repl_len = len(self.__replacement)
        if length < repl_len:
            replacement_string += self.__replacement[:length]
        else:
            amount = length // repl_len
            replacement_string += amount * self.__replacement
            if not length % repl_len == 0:
                replacement_string += self.__replacement[:length % repl_len]
        return replacement_string


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$ ")
    offensive_msg = "abc defghi mastard jklmno thisBatchCrazy"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
