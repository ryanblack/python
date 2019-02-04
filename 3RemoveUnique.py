a = [1, 2, 3, 4, 5]
b = []

for c in a:
    if a.count(c) == 1:
        b.append(c)

for c in b:
    a.remove(c)

print(a)
