'''

Given a number N followed by N numbers. Find the largest number which can be formed from the given numbers and print it.
NOTE: Each number should be used exactly once.
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
5
5 6 7 8 9
OUTPUT
98765

'''

from itertools import permutations
n = int(input().rstrip())
lis = list(input().rstrip().split())
big = 0
for i in permutations(lis):
    res = ""
    for j in i:
        res += j
    res = int(res)
    if(res > big):
        big = res
print(big)