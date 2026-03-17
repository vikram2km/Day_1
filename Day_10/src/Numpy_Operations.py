a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.array([[1,2,3]])
d = np.array([[4,5,6]])

1. np.concatenate((a,b)).shape - (6,)
2. np.stack((a,b)).shape - (2,3)
3. np.stack((a,b), axis=1).shape - (3,2)
4. np.concatenate((c,d), axis=0).shape - (2,3)
5. np.concatenate((c,d), axis=1).shape - (1,6)
6. np.vstack((a,b)).shape - (2,3)
7. np.hstack((a,b)).shape - (1,6)
8. np.column_stack((a,b)).shape - (3,2)
9. Which adds new axis → stack or concatenate? - stack
10. Which requires full shape match → stack or concatenate? - stack

#==============================================================================================
a = np.array([1,2,3])
b = np.array([[1,2,3]])
c = np.array([[1],[2],[3]])


1. shape of a  - (3,)
2. shape of b -  (1,3)
3. shape of c - (3,1)

4. a[:,None].shape - (3,1)
5. a[None,:].shape - (1,3)

6. np.expand_dims(a,0).shape - (1,3)
7. np.expand_dims(a,1).shape - (3,1)

8. np.squeeze(b).shape - (3,)
9. np.squeeze(c).shape - (3,)

10. which is column vector → a, b, or c ? - b
11. which is row vector → a, b, or c ? - c
12. which is 1D → a, b, or c ? - a

#-----------------------------------------------------------------------------
#TEST — Mandatory (Day-6 Test-3)
a = np.array([[1,2,3],[4,5,6]])
b = np.ones((2,3,4))

