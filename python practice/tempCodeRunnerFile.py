mydict = {
    "carl": 40,
    "alan": 2,
    "bob": 1,
    "danny": 3,
}

for key, value in sorted(mydict.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))