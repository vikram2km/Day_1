import numpy as np
a = np.array([
 [1,2,3],
 [4,5,6]
])

print(np.sum(a,axis=0))
print(np.sum(a,axis=1))

a = np.array([1,2,np.nan])
print(np.sum(a))
print(np.nansum(a))

a = np.array([
 [1,2,3],
 [4,5,6],
 [7,8,9]
])
#np.sum(a) - 45
#np.sum(a, axis=0) - [12, 15, 18]
#np.sum(a, axis=1) - [6,15,24]
#shape of np.sum(a, axis=0) - (3,)
#shape of np.sum(a, axis=1) - (3,)
#np.mean(a, axis=0) - [4., 5., 6.]
#np.mean(a, axis=1) - [2., 5., 8.]
#np.sum(a, axis=1, keepdims=True) shape : (3,1)
#axis removed in axis=0 ? : Row Axis
#axis removed in axis=1 ? :	Column Axis


a = np.arange(24).reshape(2,3,4)
#np.sum(a).shape : ()
#np.sum(a, axis=0).shape : (3,4)
#np.sum(a, axis=1).shape: (2,4)
#np.sum(a, axis=2).shape: (2,3)
#np.sum(a, axis=-1).shape : (2,3)
#np.sum(a, axis=(1,2)).shape: (2,)
#np.sum(a, axis=2, keepdims=True).shape : (2,3,1)
#axis removed in axis=1 ?  It will collapse rows and keeps only blocks and columns
# axis removed in axis=2 ? It will columns rows and keeps only blocks and rows
#valid axes for this array ? (0,1,2,-1,-2,-3)


a = np.array([3,7,1,7])
b = np.array([
 [1,5,3],
 [4,2,6]
])

1. np.argmax(a)
2. np.argmin(a)
3. np.max(a)
4. np.cumsum(a)
5. np.cumprod(a)

6. np.argmax(b, axis=0)
7. np.argmax(b, axis=1)
8. shape of np.argmax(b, axis=1)

9. np.sum(b*(b>3))
10. np.sum(b*(b>3), axis=1)

11. difference between sum and cumsum shape
12. what happens if argmax on empty array

a*(a>3)
a+(a>3)