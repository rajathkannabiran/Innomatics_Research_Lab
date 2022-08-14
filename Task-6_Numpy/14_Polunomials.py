import numpy

arr=numpy.array(list(map(float,input().split())))
x=int(input())
#a=arr[::-1]
print(numpy.polyval(arr,x))