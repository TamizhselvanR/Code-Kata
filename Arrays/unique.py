'''

Given a number N followed by N numbers. Out of these N numbers some of them are repeated. Write a program to find the first number which is repeated. If no numbers are repeated print 'unique'.
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
7
1 2 3 2 3 4 3
OUTPUT
2

'''

n = int(input().rstrip())
lis = list(map(int,input().rstrip().split()))
flag = 0
for i in lis:
    if(lis.count(i) > 1):
        print(i)
        flag = 1
        break
if(flag == 0):
    print("unique")
