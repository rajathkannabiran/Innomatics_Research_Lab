import numpy

n,m=map(int,input().split())
arr=numpy.array([list(map(int,input().split())) for i in range(n)])

a=numpy.min(arr, axis=1)
print(numpy.max(a))