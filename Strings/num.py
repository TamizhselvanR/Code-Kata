'''

Given a number N and a number K, check if it has all digits from 0 to k in it(take input as string).
Input Size : N <= 1000000000000000
Sample Testcase :
INPUT
1234034 4
OUTPUT
yes

'''

inp,k = input().rstrip().split()
k = int(k)
count = 0
for i in range(k+1):
    if str(i) in inp:
        count += 1
if((count - 1) == k):
    print("yes")
else:
    print("no")