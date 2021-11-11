# a - (b^2 / (c - d * (a + b)))
a = 1
b = 2
c = 3
d = 4

print(a - (b ** 2 / (c - d * (a + b))))

name = "Hans"
age = 37

greeting = f"Hello {name}, you are {age} years old!"

print(greeting)

s = "aB:cD"
kek = s.find(':')
lower = s[:kek].lower()
upper = s[kek + 1:].upper()
print(lower + s[kek] + upper)

for i in greeting:
    print(i)

karo = 69


def these_nuts(k):
    return k * k


print(these_nuts(69))
