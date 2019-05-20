import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
  level = 0
  valeycount = 0
  sealevel = 0
  for i in s:
    if i == 'U':
      level+=1
    elif i == 'D':
      level-=1
    if level < 0 and sealevel >= 0:
      valeycount+=1
      sealevel = -1
    elif level >= 0:
      sealevel = 0
  return valeycount
    

if __name__ == '__main__':
  n = 8
  s = ['U','D','D','D','U','D','U','U','D','U','D','U','U']
  print(countingValleys(n, s))
