if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    m=max(arr)
    while m in arr:
        arr.remove(m)
    print(max(arr))
    