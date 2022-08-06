# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
z = complex(input())
r = cmath.phase(z)
p = abs(z)
print(p)
print(r)