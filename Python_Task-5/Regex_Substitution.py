# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    a=input()
    while (' && ' in a) or (' || ' in a):
        a=a.replace(' && ', ' and ')
        a=a.replace(' || ', ' or ')
    print(a)