import numpy

n,m,p=map(int,input().split())
inp1=numpy.array([input().split() for i in range(n)], int)
inp2=numpy.array([input().split() for i in range(m)], int)

print(numpy.concatenate((inp1,inp2),axis=0))