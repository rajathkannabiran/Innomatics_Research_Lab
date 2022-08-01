n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    a = input().split()
    if a[0] == 'remove' or a[0] in s:
        s.remove(int(a[1]))
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    elif a[0] == 'pop':
        s.pop()

print(sum(list(s)))