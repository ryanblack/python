import random
my_randoms = random.sample(range(0, 1000), 100)
print(sorted(my_randoms, reverse=True))

listA = [0]
listB = listA
listB.append(1)
print(listA)