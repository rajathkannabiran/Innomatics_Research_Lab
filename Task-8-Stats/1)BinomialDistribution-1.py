# Enter your code here. Read input from STDIN. Print output to STDOUT
def prod(n,x):
    return factorial(n)/(factorial(x)*factorial(n-x))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n,x=6,3
b,g=map(float,input().split())
ans=0
p=b/(b+g)
q=1-p
for i in range(x,n+1):
    ans+=prod(n,i) * (p**i) * (q**(n-i))
print(round(ans,3))