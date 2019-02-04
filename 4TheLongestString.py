import re
def long_repeat(line):
    globalcount = 
    for i in range(len(line)):
        templetter = line[i]
        tempcount = line.count(templetter)
        if tempcount > globalcount:
            globalcount = tempcount


    return globalcount

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    print(long_repeat('aaskjdjaakjaaa'))