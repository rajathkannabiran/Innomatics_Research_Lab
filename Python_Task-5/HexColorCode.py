# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    s=input()
    m=list(re.findall(r'([#][a-fA-F0-9]{3,6})[;,)]{1}',s))
    for j in m:
        print(j)