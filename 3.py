import random

list1 = []
list2 = []
n = 5
for i in range(n):
    list1.append(random.randint(0, 10))
    list2.append(random.randint(0, 10))
print(list1)
print(list2)
print(list(set(list1) & set(list2)))
print(list(set(list1) - set(list2)))
print(list(set(list2) - set(list1)))
print(list(set(list1) ^ set(list2)))
