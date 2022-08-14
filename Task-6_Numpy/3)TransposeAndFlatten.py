import numpy

n,m=map(int,input().split())
inp=numpy.array([input().split() for i in range(n)], int)
print(numpy.transpose(inp))
print(inp.flatten())