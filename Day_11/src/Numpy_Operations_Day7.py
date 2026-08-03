'''a = np.array([7,2,9,1,5])
b = np.array([[3,1,2],[9,6,5]])

1. np.sort(a) - [1,2,5,7,9]
2. np.argsort(a) - [3,1,4,0,2]
3. np.sort(a)[::-1] - [9,7,5,2,1]

4. np.sort(b, axis=1) - [[3,1,2,],
                         [9,6,5]]
5. np.sort(b, axis=0) - [[1,2,3],[5,6,9]]

6. np.unique([1,2,2,3,3,3]) - [1,2,3]
7. np.unique([1,2,2,3,3,3], return_counts=True) array([1,2,3]),array([1,2,3])

8. np.diff([1,4,6,10]) - [3,2,4]

9. np.percentile([1,2,3,4,5],50) - 3

10. top 2 values of a using sort - np.sort(a)[-2:]

11. top 2 indices of a using argsort  - np.argsort(a)[-2:]

#============================================================================
a = np.array([10,3,7,1,9])
b = np.array([[4,2,3],[9,1,5]])

1. np.argsort(a) - [3,1,2,4,0]
2. a[np.argsort(a)]- [1,3,7,9,10]

3. index of max using argmax - np.argmax(a)
4. top 2 indices using argsort - np.argsort(a)[-2:]
5. top 2 values using argsort - a[np.argsort(a)[-2:]]

6. np.partition(a, 2) - [1,3,7,9,10]
7. np.partition(a, -2)[-2:] - [9,10]

8. difference between argsort and argmax - argsort will restun a series of index of elements in ascending order whereas argmax will return index os single highest element 
9. which is faster for top-k → sort or partition? - partition as it won't sort entire array.So the timecomplexity is o(n)

10. np.argsort(b, axis=1) - [[1,2,0],[1,2,0]]

#========================================================================================
a = np.array([1,2,2,3,4,4,5])
b = np.array([3,4,4,5,6])

1. np.unique(a) - [1,2,3,4,5]
2. np.unique(a, return_counts=True) - array([1,2,3,4,5]),array([1,2,1,2,1])

3. np.isin(a,[2,4]) - [False,True,True,False,True,True,False]
4. a[np.isin(a,[2,4])] - [2,2,4,4]

5. np.intersect1d(a,b) - [3,4,5]
6. np.union1d(a,b) - [1,2,3,4,5,6]
7. np.setdiff1d(a,b) - [1,2]
8. np.setdiff1d(b,a) - [6]

9. find duplicates in a using unique:
    value,count=np.unique(a,return_counts=True)
    value[count>=2]
10. find values in a not in [1,5]
    a[~np.isin(a,[1,5])]'''
#====================================================
a = np.array([10,20,30,40,50])

b = np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])

1. a[[0,2,4]] - [10,30,50]

2. b[[0,2]] - [[1,2,3],[7,8,9]]

3. b[:,[0,2]] - [[1,3],[4,6],[7,9]]

4. b[[0,1],[1,2]]

5. b[[2,0],[0,1]]

6. shape of b[[0,2]]

7. shape of b[:,[1]]

8. difference between
   b[[0,1],[1,2]]
   b[[0,1]][:,[1,2]]

9. does fancy indexing return view or copy?

10. result of
    a[[1,1,3,3]]