import numpy as np
a=np.array([1,2,3])
b=np.array([[1,2],[3,4],[5.6]])
a[0],b[0] ,b[1][1]      #finds out which element is there in that indexing#

M=np.matrix([1,2],[3,4],[5.6])
M       #PRINTS THE SAME ARRAY IN MATRIX FORM#

c=b.T
print(c)            # transpose

print(c.shape)         #shows size of the array#

print(a.ndim)         #shows the dimension
print(b.ndim)             of the array#

print(b.size)           #shows how many
print(a.size)              #  elements are present

print(a.dtype)            #gives datatype
print(b.dtype)              # of the array#

print(b.itemsize)                #shows how many bytes it takes for example integer takes 4 bytes#

d=np.array([1.1,2.2,3.3])
print(d.dtype)                   #shows datatype# #this is an example of float#

e=np.array([1,2], dtype=np.float64)
print(e)                                      #typecast the array to float#

print(e.itemsize)          #shows how many bytes it takes#

print(b.min())    #shows the minimum value#
print(b.max())      #shows the maximum value#

print(b.sum())        #sum of the araay b#
print(b.sum(axis=0))   #sum of vertical elements of array#
print(b.sum(axis=1))    #sum of horizontal#