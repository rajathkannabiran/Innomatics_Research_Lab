# Enter your code here. Read input from STDIN. Print output to STDOUT
a=set(map(int,input().split()))
n=int(input())
c=0
for i in range(n):
    s=set(map(int,input().split()))
    if len(s.difference(a)) == 0 and len(s) != len(a):
        c+=1
if c==n:
    print("True")
else:
    print("False")
        