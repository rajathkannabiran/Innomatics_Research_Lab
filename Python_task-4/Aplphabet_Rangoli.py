def print_rangoli(size):
    # your code goes here
    li = []
    j = ((size*2)-1)+((size*2)-2)
    import string
    ch = string.ascii_lowercase[:size]
    for i in range(1, size+1):
        li.append("-".join(ch[::-1][:i]+ch[::-1][:i][::-1][1:]).center(j, "-"))
    for i in range(size-1,0,-1):
        li.append("-".join(ch[::-1][:i]+ch[::-1][:i][::-1][1:]).center(j, "-"))
    print("\n".join(li))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)