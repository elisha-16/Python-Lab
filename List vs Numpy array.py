import numpy as np
L=[1,2,3]
NA=np.array(L)
for i in L:
	print(i)

for i in NA:
	print(i)

L1=L+[4,5,6]   #to append to a list#
print(L1)

L1.append(7)   #to append a new element#
print(L1)

NA2=NA+[8]     #it will sum=vector addition#
print(NA2)

NA3=NA+NA      #vector addition#
print(NA3)

L4=[]
for i in L:
	L4.append(i+i)                #vector addition in list#
print(L4)

  2*NA      #multiply 2 with numpy array#

  2*L       #print L named list 2 times or concatinate two list#

 NA**2     #print the squares of numpy array elements#

 L**2      #error#

for i in L:              #print the squares of list#
	print(i*i)

np.sqrt(NA)       #finds out squareroots of numpy array#

np.log(NA)      #finds out log of each element in numpy array#

np.exp(NA)     #exponential of elements of numpy array#