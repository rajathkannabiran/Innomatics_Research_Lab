# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
na = set(map(int, input().split()))
m = int(input())
ma = set(map(int, input().split()))

f = list((na.union(ma)) - (na.intersection(ma)))

for i in sorted(f):
    print(i)