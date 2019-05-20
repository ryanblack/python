def repeatedString(s, n, c):
  round=n//len(s)
  rest=n-round*len(s)
  return s.count(c)*round+s[0:rest].count(c)
if __name__ == '__main__':
  n=1000000000000000000
  s='aaaabbb'
  c='a'
  #repeatedString(s, n, c)
  print(repeatedString(s, n, c))