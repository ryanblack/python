def polydrome(str):
  length = len(str)
  i=0
  result=True
  while i < length//2 and result==True:
    if str[i] != str[length-i-1]:
      result=False
    i+=1
  return result

if __name__ == "__main__":
  str1='racecar'
  str2='mommymom'
  str3='kuhcchuk'
  print("str1=",str1,"is", 'a Polydrome' if polydrome(str1) else 'Not a Polydrome')
  print("str1=",str2,"is", 'a Polydrome' if polydrome(str2) else 'Not a Polydrome')
  print("str1=",str3,"is", 'a Polydrome' if polydrome(str3) else 'Not a Polydrome')