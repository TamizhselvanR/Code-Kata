'''

Given a number N and array of N integers, print the difference between the indices of smallest and largest number(if there are multiple occurances, consider the first occurance).
Input Size : |N| <= 1000000
Sample Testcase :
INPUT
5
3 5 4 4 7
OUTPUT
4

'''

n = input().strip()
lis = list(map(int, input().strip().split()))
a = lis.index(max(lis))
b = lis.index(min(lis))
if (a > b):
    print(a - b)
else:
    print(b - a)
