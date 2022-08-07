# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
m=re.findall(r'[qwrtypsdfghjklzxcvbnm]([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])',s,re.IGNORECASE)
if m:
    for i in m:
        print(i)
else: print(-1)