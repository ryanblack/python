def oddnumber(l, k):
  while l <= k:
    odd = l%2
    if odd > 0 :
      print(l)
    l += 1
  
if __name__ == '__main__':
  l = 0
  k = 56
  oddnumber(l, k)