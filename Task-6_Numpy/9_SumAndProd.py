import numpy

n,m=map(int,input().split())
arr=numpy.array([list(map(int,input().split())) for i in range(n)])

a=numpy.sum(arr, axis=0)
print(numpy.prod(a))