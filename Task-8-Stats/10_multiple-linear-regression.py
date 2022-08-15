import numpy as np
m,n = [int(i) for i in input().split(' ')]
x,y = [],[]

for i in range(n):
    data = input().strip().split(' ')
    x.append(data[:m])
    y.append(data[m:])
q = int(input().strip())
X_new = []
for i in range(q):
    X_new.append(input().strip().split(' '))
x = np.array(x,float)
y = np.array(y,float)
X_new = np.array(X_new,float)

X_R = x-np.mean(x,axis=0)
Y_R = y-np.mean(y)

beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)),np.dot(X_R.T,Y_R))

X_new_R = X_new-np.mean(x,axis=0)
Y_new_R = np.dot(X_new_R,beta)
Y_new = Y_new_R + np.mean(y)

for i in Y_new:
    print(round(float(i),2))