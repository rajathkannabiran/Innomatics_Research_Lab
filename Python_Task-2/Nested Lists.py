if __name__ == '__main__':
    li=[]
    di={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name,score])
        if score not in di:
            di[score] = [name]
        else:
            di[score].append(name)
    f=list(di.keys())
    m=min(di.keys())
    while m in f:
        f.remove(m)
    m=min(f)
    for i in sorted(di[m]):
        print(i)
    