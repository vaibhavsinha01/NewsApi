import numpy as np

"""#basic functions
arr=np.array([[1,2,3,4],[5,6,7,8],[1,3,5,7]])
print(arr)
print(type(arr))
print(arr[0:2])
print(arr[2][3])"""

"""#indexing
arr=np.array([[10,20,30,40],[50,60,70,80]])
print(arr[0:2,0:2])#this gives the first 2 elements of each
print(arr[0][0:2],arr[1][0:2])"""

"""#size/shape functions
arr=np.array([[10,20,30,40],[50,60,70,80],[10,30,50,70]])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)"""
"""
#np functions

#1.the arange function has starting value ending value and the step value 
print(np.arange(3,18,2,dtype=float))
#2.zeros and ones function fills the function with zeros or one
print(np.zeros((3,3),dtype=int))
print(np.ones(7,dtype=float))#here default dtype=float
#3.returns a new array with same shape and type with a given fill value
print(np.full((4,3),9,dtype=int))
#reshape changest the shape of a functin without changing the data of a array
print(np.arange(6).reshape(2,3))
print(np.arange(9).reshape(-1))
print(np.arange(10).reshape(2,-1))#pass -1 if don't know about size 

"""
"""
#np functions

#1.repeat function
arr=np.repeat([3],5,axis=0)
arr1=np.repeat([[4,3]],5,axis=1)
arr3=np.repeat([[3,4]],5,axis=1)
arr2=np.repeat([[3,2]],5,axis=0)
#2.concatenate function
c=np.concatenate([arr3,arr1])
arr4=np.array([[1,4,5,6],[1,4,5,9]])
arr5=np.array([[4,5,6,7],[2,5,7,9]])
d=np.concatenate([arr4,arr5],axis=1)
print(d)
#hstack and vstack
print(np.vstack([arr4,arr5]))
print(np.hstack([arr4,arr5]))

"""
"""
#np functions
#1.power
arr=np.array([1,2,3,4])
print(np.power(arr,[2]))
print(np.power(arr,[5]))
print(np.power(arr,[1,3,3,2]))
#2.diff
arr1=np.array([1,5,8,3])
arr2=np.array([2,7,3,5])
print(np.diff(arr1))#general formula is n2-n1,n3-n2,n4-n3 and so on
print(np.diff((arr1,arr2),axis=0))
#3.cross
arr3=np.array([1,5])
arr4=np.array([2,7])
print(np.cross(arr3,arr4))
#4.sort
arr5=np.array([1,9,4,8])
arr6=np.array([2,7,4,5])
print(np.sort((arr5,arr6),axis=0))
print(np.sort((arr5,arr6),axis=1))

"""
"""
#np functions
#1.flatten
n1=[2,4,6,8]
n2=[1,3,5,7]
n=(np.array([n1,n2]))
print(n.flatten())
print(n.flatten('C'))
print(n.flatten('F'))
print(n.flatten('A'))
print(n.flatten('K'))
#2.sum
print(n.sum())
print(n.sum(axis=1))
#3.nansum-used to convert NaNs to 0
n3=[2,4,6,np.nan]
n4=[1,3,5,7]
n5=(np.array([n3,n4]))
print(n5.sum(axis=1))
print(np.nansum(n5,axis=1))
#4.cumprod
print(n.cumprod())
#5.cumsum
print(n.cumsum())

"""
"""
#numpy iteration functions
arr=np.array([[[1,2],[3,8]],[[5,1],[8,2]]])
for i in arr:
    for j in i:
        for k in j:
            print(k)

#method 2
arr=np.array([[[1,2],[3,8]],[[5,1],[8,2]]])
for i in np.nditer(arr):
    print(i)

#method 3
for ind,i in np.ndenumerate(arr):
    print(ind,i)
"""

"""
#copy/view function 
#the main difference between the copy and the view function is that copy is a new array while the view function is view of original array
arr=np.array([2,6,2,8,1])
c=np.copy(arr)
v=arr.view()
arr[2]=7
print("Original:",arr)
print("Copy:",c)
print("View",v)

"""
"""
arr=np.array([1,2,4,2,5,1])
s=np.array_split(arr,2)
t=np.array_split(arr,3)
u=np.array_split(arr,4)
arr1=np.array([[1,2,4],[2,5,1]])
v=np.array_split(arr1,4,axis=1)
print(s)
print(t)
print(u)
print(v)
"""
"""
#1.sort
arr=np.array([[2,5,7,8,3],[2,8,3,7,2]])
print(np.sort(arr))
print(np.sort(arr,axis=0))
#2.search
arr1=np.array([1,6,5,2,6,8,2])
print(np.where(arr1==6))
print(np.where(arr1%2==0))
print(np.where(arr1!=6))
#3.searchsorted-works on the sorted value only
arr2=np.array([1,3,5,7,9])
ss=np.searchsorted(arr2,5)
print(ss)
#4.filter
arr3=np.array([3,6,2,6,8])
fa=[True,False,True,True,False]
print(arr3[fa])
arr4=np.array([2,6,3,6,8,3,6,9,2])
fa1=arr4>5
new=arr4[fa1]
print(new)

"""
"""
#numpy functions
#1.insert
arr=np.array([20,40,60,80])
print(arr)
#2.delete
print(np.insert(arr,2,50))
print(np.insert(arr,(1,2,4),50))
arr2=np.array([[20,40],[60,80]])
print(arr2)
print(np.insert(arr2,1,50,axis=1))
print(np.insert(arr2,1,50,axis=0))
print(np.insert(arr2,1,[50,40],axis=0))

arr3=np.array([20,50,30,60,20,40])
print(arr3)
print(np.delete(arr3,4))
arr4=np.array([[20,50,30],[60,20,40]])
print(arr4)
print(np.delete(arr4,1,axis=0))
print(np.delete(arr4,1,axis=1))
"""
