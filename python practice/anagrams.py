import math
from itertools import permutations 
from collections import Counter
def sherlockAndAnagrams(s):
  pairs = 0
  #all different
  res = [i for i in s if s.count(i)>1]
  if res == []:
    print('We have all Different!')
  #count all by 1character, like kkkk, iiidkdkrrrr
  result=Counter(res)
  #print( result)
  for k, v in result.items():
    pairs+=(v-1)*v//2
  #print(pairs)
  #count others by more than 1
  print('One letter repeats! Pairs = ', pairs)
  i = 3
  itemp=''
  while i < len(s):
    itemp=s[0:i]   #ifa
    #print(itemp)
    jtemp=''
    permList = permutations(itemp)
    tlist=list(permList)
    tempdel=tlist[0]
    for t in tlist:
      if t==tempdel:
        tlist.remove(t)
    #del tlist[0]
    #print(tlist)               
    print('=====================')
    for perm in tlist:
      jtemp=''.join(perm)
      if jtemp in s:
        pairs+=1
        print(tlist)
        print(jtemp,'- found in ', s)
    i+=1
  print('Permutation found! Pairs = ', pairs)

if __name__ == '__main__':
  s='iiii'
  sherlockAndAnagrams(s)
  #print(sherlockAndAnagrams(s))