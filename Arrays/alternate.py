'''

n = int(input().rstrip())
lis = list(map(int,input().rstrip().split()))
lis.sort()
rev = lis[::-1]
count = 0
a = 0
s = n - 1
while(count < n):
 print(rev[a],end = " ")
 count += 1
 if(count == n):
  break
 print(lis[a],end = " ")
 count += 1
 a += 1

'''

n = int(input().rstrip())
lis = list(map(int,input().rstrip().split()))
lis.sort()
rev = lis[::-1]
count = 0
a = 0
s = n - 1
while(count < n):
 print(rev[a],end = " ")
 count += 1
 if(count == n):
  break
 print(lis[a],end = " ")
 count += 1
 a += 1