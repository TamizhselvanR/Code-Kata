'''

You are given string ‘s’. Your task is to modify the string as mentioned below:-
1)The string should not have three consecutive same characters.
2)You can add any number of characters anywhere in the string. Find the minimum number of characters which Ishaan must insert in the string.

Sample Input :
aabbbcc

Sample Output :
1

'''

from itertools import groupby
a = input().rstrip()
count = 0
for i,j in groupby(a):
 length = len(list(j))
 if(length > 2):
  count += length // 2
print(count)