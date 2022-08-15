# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def central(x, mu, sig):
    Z = (x - mu)/sig
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

x = int(input())
n = int(input())
mu = int(input())
sig = int(input())
mu_sum = n * mu 
sig_sum = math.sqrt(n) * sig

print(round(central(x, mu_sum, sig_sum), 4))