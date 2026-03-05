import numpy as np
'''
a=np.array([1,2,3,4,5])
print(a.size," ",a.shape," ",a.dtype," ",a.ndim)

b = np.array([[1,2,3],[4,5,6]])
print(b.size," ",b.shape," ",b.dtype," ",b.ndim)

#direct multiplication
print(np.array([1,2,3]) * 2)
print(b*2)

#sum
print(a.sum(), b.sum())
#mean
print(a.mean(), b.mean())
'''


#Problems
data=np.array([10, 20, 30, 40, 50])
#1. Multiply by 2
print(data*2)
#2.compute mean
print(data.mean())
#3.compute sum
print(data.sum())
#4.reshape to (5,1)
print(data.reshape(1,5))

