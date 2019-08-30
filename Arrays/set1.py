'''

Given 2 numbers N,K and N arrays each of size K, print the elements that have appeared in all arrays.
Input Size : 2 <= N, K <= 100000
Sample Testcases :
INPUT
2 3
1 0 2
0 8 7
OUTPUT
0

'''

from itertools import combinations
n,k = map(int,input().rstrip().split())
lis = set()
for i in range(n):
 if(i == 0):
  lis.update(input().rstrip().split())
 else:
  lis = lis.intersection(input().rstrip().split())
for i in lis:
 print(i,end = " ")