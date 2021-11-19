from Week9_Dog_Exercise1 import Dog

doglist = []
fido = Dog("Fido", "Poodle", 3, 'female')
these = Dog("these", "Wolf", 2, 'male')
nuts = Dog("nuts", "Wolf", 1, 'female')
lul = Dog("lul", "Bruh", 6, 'male')

doglist.append(fido)
doglist.append(these)
doglist.append(nuts)
doglist.append(lul)

newdog = fido + these
doglist.append(newdog)
print(doglist[-1].breed)
print(doglist[-1].sex)
newdog = these + nuts
doglist.append(newdog)
print(doglist[-1].breed)
print(doglist[-1].sex)
newdog = these + lul
print(newdog)

fido.learn_trick("yeeting off the bridge")
print(fido.tricks)
fido.learn_trick("bite off D")
print(fido.tricks)
