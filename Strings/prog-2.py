"""

Given a string S and a number K. Print all the substrings of S of length K(space separeted output).
Input Size : |S| <= 100 and K<= 50
Sample Testcase :
INPUT
prog 2
OUTPUT
pr ro og

"""

inp, a = input().rstrip().split()
a = int(a)
count = 0
for i in range(len(inp) - 2 + 1):
    print(inp[i], end="")
    for j in range(1, a):
        print(inp[i + j], end="")
    print(" ", end="")
