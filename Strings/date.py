'''

Accept a string and find if it is of date format 'dd/mm/yyyy'.
Sample Testcase :
INPUT
01/13/1999
OUTPUT
no

'''

inp = input().rstrip()
if(len(inp) == 10 and inp[2] == "/" and inp[5] == '/'):
  if(int(inp[0:2]) < 32 and int(inp[3:5]) < 13):
    print('yes')
  else:
    print('no')