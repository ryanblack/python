def jumpingOnClouds(c):
  steps = 0
  i=0
  l = len(c)-1
  while i+2 != l and i+1 != l:
    if c[i] == 0 and c[i+2] == 0:
      steps+=1
      i+=2
    elif c[i] == 0 and c[i+1] == 0:
      steps+=1
      i+=1
  steps+=1
  return steps

if __name__ == '__main__':
  c = [0,1,0,0,0,0,1,0,1,0,1]
  print(jumpingOnClouds(c))