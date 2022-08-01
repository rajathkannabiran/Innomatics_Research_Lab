if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(N):
        a = list(input().split())
        if a[0] == 'insert':
            li.insert(int(a[1]),int(a[2]))
        elif a[0] == 'print':
            print(li)
        elif a[0] == 'remove':
            li.remove(int(a[1]))
        elif a[0] == 'append':
            li.append(int(a[1]))
        elif a[0] == 'sort':
            li.sort()
        elif a[0] == 'pop':
            #z = li[-1]
            li.pop(-1)
        elif a[0] == 'reverse':
            li.reverse()