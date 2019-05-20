def findNumber(arr, k):
  for i in arr:
    if i == k :
      return "yes"
  return "no"

if __name__ == '__main__':
  arr = [3,46,3,9,8,9,5,4,4,76,5,4]
  k = 56

  print(findNumber(arr, k))