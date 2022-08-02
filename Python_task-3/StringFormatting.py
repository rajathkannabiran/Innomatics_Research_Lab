def print_formatted(number):
    # your code goes here
    space= len(bin(number)[2:])
    for i in range(1,number+1):
        d = str(i)
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
        print(d.rjust(space), o.rjust(space), h.rjust(space), b.rjust(space))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)