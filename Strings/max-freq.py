'''

Given a string of length N, print the most repeated letter(It is guarenteed that a single answer is possible).
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
Vishal Yadav
OUTPUT
a

'''

from collections import Counter
inp = list(map(str,input().rstrip()))
big = 0
for i,j in Counter(inp).items():
    if(j > big):
        big = j
        ans = i
print(ans)