import numpy

n,m=map(int,input().split())
arr=numpy.array([list(map(int,input().split())) for i in range(n)])

print(numpy.mean(arr, axis=1))
print(numpy.var(arr,axis=0))
print(round(numpy.std(arr),11))