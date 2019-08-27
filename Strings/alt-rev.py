'''

Given a string print reverse all words except the first and last words.
Sample Testcase :
INPUT
Hi how are you
OUTPUT
Hi woh era you

'''

inp = list(input().rstrip().split())
for i in range(len(inp)):
  if(i == 0 or i == len(inp)-1):
    print(inp[i],end = " ")
  else:
    print(inp[i][::-1],end = " ")
