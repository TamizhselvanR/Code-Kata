'''

Given N strings and a prefix string p. Find how many of the N strings have p as their prefix.
for eg: String[] input={'100','111','10100','10','1111'} prefix='10'
output=2
Input Size : N <= 100000, string length <=1000, prefix length <=100
Sample Testcase :
INPUT
5
100 111 10100 10 1111
10
OUTPUT
3

'''

a = input().rstrip()
inp = list(input().rstrip().split())
c = input().rstrip()
le = len(c)
count = 0
for i in inp:
 if(c == i[0:len(c)]):
  count += 1
print(count)