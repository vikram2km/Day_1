import numpy as np

#Problems
arr = np.array([5, 10, 15, 20, 25, 30])
#1. Get elements greater than 15.
print(arr[arr>15])
#Normalize array to range [0,1]
print([(arr-min(arr))/(max(arr)-min(arr))])
#Reshape into (2, 3)
print(arr.reshape(2,3))

a = np.array([1,2,3])
b = np.array([[10],[20],[30]])
print(a+b)




