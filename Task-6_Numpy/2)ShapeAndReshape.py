import numpy

inp=list(map(int,input().split()))
arr=numpy.array(inp)
ans=arr.reshape(3,3)
print(ans)