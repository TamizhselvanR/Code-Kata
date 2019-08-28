'''

A number is given as input. Find the maximum number that can be formed using the digits.
Input Size : N <= 10000000
Sample Testcase :
INPUT
4123
OUTPUT
4321

'''

from itertools import permutations
inp = list(map(str,input().rstrip()))
big = 0
for i in permutations(inp):
    a = "".join(i)
    if(int(a) > big):
        big = int(a)
print(big)