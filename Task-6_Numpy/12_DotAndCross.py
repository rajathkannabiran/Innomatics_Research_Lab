import numpy

n=int(input())
arr1=numpy.array([list(map(int,input().split())) for i in range(n)])
arr2=numpy.array([list(map(int,input().split())) for i in range(n)])

print(numpy.matmul(arr1,arr2))