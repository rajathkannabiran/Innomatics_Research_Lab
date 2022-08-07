# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
k=input()
sub=re.compile(k)
m=sub.search(s)
if m:
    while m:
        x=m.start()
        print((x, m.end()-1))
        m=sub.search(s,x+1)
else:
    print((-1, -1))