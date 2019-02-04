import re
def checkio(str):

    if re.search("[a-z]+", str) and re.search("[A-Z]+", str) and re.search("[0-9]+", str) and (10 <= len(str)):
        return True
    else:
        return False

if __name__ == '__main__':
    result = checkio('1234Aa04444333dd0')
    print(result)
