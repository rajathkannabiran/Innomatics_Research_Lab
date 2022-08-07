# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
n=int(input())
for i in range(n):
    inp=input()
    a,b=email.utils.parseaddr(inp)
    if re.search("^[a-z][\w\d.,-_]+@[a-z]+\.[a-z]{1,3}$",b,re.I):
        print(inp)