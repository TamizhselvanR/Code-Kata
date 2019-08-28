'''

The longest common prefix for N strings of length at most M each is defined as a string K
Such that every string has K as a prefix.
You are given the task of finding the longest common prefix for N such strings.

Constraints:

1<=N<=10000

1<=M<=100

Sample Input :
4
abcdjkhkjh
ahhjk
abcdhjjj
aa

Sample Output :
a
'''
n = int(input().rstrip())
small = 100
lis = []
for _ in range(n):
    inp = input().rstrip()
    lis.append(inp)
    if(len(inp) < small):
        small = len(inp)
i = 1
while(i <= small):
    new = []
    for j in lis:
        new.append(j[0:i])
    se = set(new)
    if(len(se) == 1):
        ans = se.pop()
    i += 1
print(ans)