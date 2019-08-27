'''

Given a number N followed by an array of N integers, replace every element with the greatest element on the right side(to that element) in the array. Replace last element with 0 as there no element on the right side of it.
eg. if the array is {6, 7, 4, 3, 5, 2}, output {7, 5, 5, 5, 2, 0}.
Input Size : N <= 100000
Sample Testcase :
INPUT
6
6 7 4 3 5 2
OUTPUT
7 5 5 5 2 0

'''

n = int(input().rstrip())
lis = list(map(int,input().rstrip().split()))
for i in range(len(lis)-1):
 j = i + 1
 print(max(lis[j:]),end = " ")
print("0")