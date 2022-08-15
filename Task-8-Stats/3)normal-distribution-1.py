# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def nodi(x,m,s):
    f=(x-m)/(s*math.sqrt(2))
    return (1+math.erf(f))/2
    
m,s=20,2

print(round(nodi(19.5,m,s),3))
print(round(nodi(22,m,s) -nodi(20,m,s),3))