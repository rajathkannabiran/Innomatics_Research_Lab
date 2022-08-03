def swap_case(s):
    ans = ""
    for i in s:
        if i.islower():
            f = i.upper()
        elif i.isupper:
            f = i.lower()
        ans += f
    return ans

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result