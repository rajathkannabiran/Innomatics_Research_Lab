import numpy

numpy.set_printoptions(legacy='1.13')
n = int(input())
arr = numpy.array([input().split() for i in range(n)], float)
print(numpy.linalg.det(arr))