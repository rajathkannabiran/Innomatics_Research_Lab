def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    sub=(string[i:i+k] for i in range(0,n,k))
    for i in sub:
        arr=[]
        arr.append(i[0])
        for j in range(1,len(i)):
            if i[j] not in arr:
                arr.append(i[j])
        print(''.join(str(z) for z in arr))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)