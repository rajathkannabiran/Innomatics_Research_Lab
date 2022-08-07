# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n=int(input())
c1 = r'[456]\d{3}(-?\d{4}){3}$'
c2 = r'((\d)-?(?!(-?\2){3})){16}'
pattern=c1, c2
for i in range(n):
    inp=input()
    print('Valid') if all(re.match(p, inp) for p in pattern) else print('Invalid')