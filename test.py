result_one = 2 + 2 + 5 * 10 ** 2
print(result_one)
result_two = (1 + 10 ** 3) * (2 + 5 ** 2)
print(result_two)
result_three = (1 + 10) ** (0.5) - (1 + 10) ** 3
print(result_three)

name = input("what is your name? ")
age = input("what is your age? ")
occupation = input("what is your occupation? ")

print(f"Hi {name}! I see you are {age} years old and work as a {occupation}.")

amount = int(input("Pls type an number from 1 to 99 "))
quarters = amount // 25
rest = amount % 25
dime = rest // 10
rest %= 10
nickel = rest // 5
rest %= 5
pennies = rest // 1

print(f'we can combine it as {quarters} quarters, {dime} dimes, {nickel} nickel and {pennies} pennies')

start = "Hello, new world!"
space = start[6]
apo = start[5]
excl = start[-1]
end = (start[4].upper() + start[0].lower() + apo + space + start[0].lower() + start[1] + start[2] * 2 + space + start[
    7] + start[4] + excl * 3)
print(end)

