import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    ans=numpy.array(arr,float)
    return ans[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)