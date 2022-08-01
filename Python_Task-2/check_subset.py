# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    a=int(input())
    arr=set(map(int,input().split()))
    b=int(input())
    brr=set(map(int,input().split()))
    if len(arr.difference(brr)) == 0:
        print("True")
    else:
        print("False")