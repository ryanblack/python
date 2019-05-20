i=100
a=0
b=0
c=0
while i < 999:
  c=i%10
  b=i%100//10
  a=i//100
  if i == (a**3+b**3+c**3):
    print(i)
  i+=1