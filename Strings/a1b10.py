'''

Write a program to give the following output for the given string S of size N.(character containing even number of occurences should be elaborated else print the same format)
Eg 1: Input: a1b10
Output: a1bbbbbbbbbb
Eg: 2: Input: b3c6d15
Output: b3ccccccd15
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
a1b10
OUTPUT
a1bbbbbbbbbb

'''

st = input().rstrip()
for i in range(len(st) - 1):
  if(st[i].isalpha()):
    count = i+1
    num = 0
    while(st[count].isdigit()):
      num = num * 10 + int(st[count])
      count += 1
      if(count == len(st)):
        break
    if(num % 2 == 0):
      print(st[i]*num,end = "")
    else:
      print("{}{}".format(st[i],num),end = "")
