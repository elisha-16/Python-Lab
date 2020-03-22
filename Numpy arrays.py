import numpy as np
np.zeros((2,3))        #the array will have specific dimension and each element will be 0#

 np.ones((3,3))           #the array will have specific dimension and each element will be 1#

 np.empty((2,3) dtype=np.int16)   #returns the array of specific shape and datatype without initializing entries#

np.arange(0,20,5)                #returns evenly spaced array within a given interval#

np.linspace(1,20)          #gives an array with specific range with evenly spaced element#
np.linspace(1,20,20)        #third arguments specifies number of element otherwise it will return 50 element #

np.random.random((2,3))   #returns an array with random value in between 0 to 1#

c = np.zeros((2, 3))
c.reshape((3,2))         #gives a new shape to the array without changing its elements#

g=np.zeros((3,3))
h = np.ones((1, 3))
o=np.vstack((g,h))       #concatenate two arrays vertically#

 e = np.ones((3, 3))
 f=np.zeros((3,1))
 w=np.hstack((e,f))    #concatenate two arrays horrizontally#

np.hsplit(o,3)    #split array horrizontally with specific different arrays#
np.vsplit(w,5)     #split array vertically with specific different arrays#

a=np.identity(3)      #returns the identity array#

d=np.full(4,0.6)    #return an array with given shape and fill value#

 np.logspace(0, 10)    #returns evenly spaced number on a log scale#

 

