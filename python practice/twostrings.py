def twoStrings(s1, s2):
  if [i for i in s1 if i in s2]:
    return 'YES'
  else: return 'NO'
if __name__ == '__main__':
  s1='Con'
  s2='Aha'
  print(twoStrings(s1, s2))


'''   
Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

Function Description
======================
Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

twoStrings has the following parameter(s):

s1, s2: two strings to analyze .

Input Format
============
The first line contains a single integer p, the number of test cases.

The following p pairs of lines are as follows:

The first line contains string s1.
The second line contains string s2. '''