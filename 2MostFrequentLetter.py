import re
if __name__ == '__main__':
    str = ("jladjdliLDIDKD")
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    str = str.lower()
    tempcount = 0
    globalcount = 0
    globalletter = ''
    for i in range(len(str)):
        #print("Trying letter:", str[i])
        if str[i] != globalletter:
            for c in str:
                if str[i] == c and bool(re.search("[a-z]+",str[i])):
                    tempcount += 1
                    templetter = str[i]
            #        print("tempcount:", tempcount, templetter, bool(re.search("[a-z]+",str[i])))
            #print("Compare temp with global:", tempcount, '>=', globalcount, 'and', templetter, '<', globalletter)
            if tempcount == globalcount and alfabet.index(templetter) < alfabet.index(globalletter):
                globalletter = templetter
                globalcount = tempcount
            elif tempcount > globalcount:
                globalletter = templetter
                globalcount = tempcount

            print("Compare result - Letter : ", globalletter, globalcount, 'is chosen')
            tempcount = 0
            #print("Reset tempcount:", tempcount)
            #print("=============================================")
        i += 1
    print("Most frequent Letter is:",globalletter, globalcount)

#Alternative
"""
import string

def checkio(text):

    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.

    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
"""
