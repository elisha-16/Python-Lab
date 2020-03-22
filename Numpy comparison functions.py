import numpy as np
a=np.array([1,2,3,4])
b=np.array([10,20,30,40])

print(np.greater(b,a))     #return the truth value(b>a) element wise#

print(np.less(a,b))       #return the truth value(a<b) element wise#

print(np.equal(a,b))      #return the truth value(a=b) element wise#

print(np.not_equal(a,b))    #(a=!b)

print(np.greater_equal(a,b))   #returns (a>=b)

print(np.less_equal(b,a))     #returns (a<=b)