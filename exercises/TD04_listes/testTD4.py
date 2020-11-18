import random

list2 = []

for i in range(0, 10):
    a = (random.randint(10, 99))
    list2.append(a)

print(list2)


list2_pairs = list2.copy()
list2_impairs = list2.copy()

for i in range(1, 2):
    if list2[i] % 2 != 0:
        del list2_pairs[i]


print(list2_pairs)
print(list2_impairs)