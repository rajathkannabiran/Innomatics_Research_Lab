# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(int,input().split()))
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
a=list(d.keys())
b=list(d.values())
print(a[b.index(min(b))])