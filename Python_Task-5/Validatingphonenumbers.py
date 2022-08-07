# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    a=input()
    if len(a)!=10:
        print('NO')
    elif re.match(r'^[987]\d{9}',a):
        print('YES')
    else:
        print('NO')