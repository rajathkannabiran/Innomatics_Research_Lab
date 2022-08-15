# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def nodi(x,m,s):
    f=(x-m)/(s*math.sqrt(2))
    return (1+math.erf(f))/2
    
m,s=70,10

print(round((1-nodi(80,m,s))*100,2))
print(round((1-nodi(60,m,s))*100,2))
print(round(nodi(60,m,s)*100,2))