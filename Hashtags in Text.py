#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def analyze(posts):
    dic = {}
    for string in posts:
        last = False
        before = 0
        while not last:
            newString = string[before:]
            tag = newString.find('#')
            if tag == -1:
                last = True
                continue
            else:
                before += tag + 1
                if len(newString[tag:]) > 1:
                    if newString[tag + 1].isalpha():
                        index = tag + 2
                        hashtag = True
                        for letter in newString[tag+2:]:
                            if not newString[index].isalnum():
                                break
                            index += 1
                        word = newString[tag + 1:index]
                        if word in dic:
                            temp = dic.get(word)
                            dic.update({word: temp + 1})
                        else:
                            dic[word] = 1
    return dic


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3", "bruh .#c. these nuts #", "#k #5 #. #sugondese69", "#", "#! ,.e#lulz- NUTS"]

print(analyze(posts))
