# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int,input().split()))
m = int(input())

for i in range(m):
    k = input().split()
    b = set(map(int, input().split()))
    if k[0] == 'intersection_update':
        a.intersection_update(b)
    elif k[0] == 'update':
        a.update(b)
    elif k[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(b)
    elif k[0] == 'difference_update':
        a.difference_update(b)
print(sum(a))