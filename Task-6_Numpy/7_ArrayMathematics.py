import numpy

n,m=map(int,input().split())
arr1=numpy.array([list(map(int,input().split())) for i in range(n)])
arr2=numpy.array([list(map(int,input().split())) for i in range(n)])

print(numpy.add(arr1,arr2))
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)