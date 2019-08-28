'''

Given 2 strings S and M, check whether they have same number of characters if not make the longer string shorter to the same size of the smaller one by deleting characters from the end and concatinate them and print it.
Sample Testcase :
INPUT
rknagar vishal
OUTPUT
rknagavishal

'''

a,b = input().rstrip().split()
if(len(a) > len(b)):
 print("{}{}".format(a[0:len(b)],b))
elif(len(a) < len(b)):
 print("{}{}".format(a,b[0:len(a)]))
else:
 print("{}{}".format(a,b))