'''

Design an algorithm to accept 2 strings A and B from the user, and check whether any part of string A (comprising of minimum of 2 consecutive characters) is a sub-string of string B.
Input Size : A<=1000, B<=1000
Example:
INPUT
abcxyz hagsaabc
OUTPUT
yes

'''

flag = 0
a,b = input().rstrip().split()
for i in range(len(a)-1):
  an = a[i]+a[i+1]
  if an in b:
    print("yes")
    flag = 1
    break
if(flag == 0):
    print("no")