# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t=int(input())
rep=r'(?!.*(.).*\1)' 
up=r'(?=(?:.*[A-Z]+){2,})'
dig=r'(?=(?:.*\d){3,})'
alnum=r'[\w]{10}'
pattern=[rep, up, dig, alnum]

for i in range(0, t):
    uid = input()
    print('Valid') if all([re.match(j, uid) for j in pattern]) else print('Invalid')