from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
]


def reverse_index(dataset):
    index_dictionary = {}
    index = 0
    for string in dataset:
        string = string.lower()
        for word in string.split():
            if word in index_dictionary:
                list = index_dictionary.get(word)
                list.append(index)
                index_dictionary.update({word: list})
            else:
                index_dictionary.update({word: [index, ]})
        index += 1
    return index_dictionary
    # don't forget to return your resulting dictionary


# You can see the output of your function here
print(reverse_index(dataset))
