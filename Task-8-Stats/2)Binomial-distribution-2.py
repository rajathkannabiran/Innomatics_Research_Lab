# Enter your code here. Read input from STDIN. Print output to STDOUT
def prod(n,x):
    return factorial(n)/(factorial(x)*factorial(n-x))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
b,n=map(int,input().split())
ans1,ans2=0,0
q=b/100
p=1-q

for i in range(3):
    ans1+=prod(n,i) * (q**i) * (p**(n-i))
print(round(ans1,3))

for i in range(2,n+1):
    ans2+=prod(n,i) * (q**i) * (p**(n-i))
print(round(ans2,3))