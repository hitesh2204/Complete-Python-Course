# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:13:26 2018

@author: Hitesh
"""

import numpy as np
a=np.array([1,2,3,4,5])#array contains a list.
print(a)


#porvide one dimentional array.
import numpy as np
a=np.array([[1,2],[3,4]])
print(a)

#Gives a minimum dimentions of array.
import numpy as np
a=np.array([1,2,3,4,5],ndmin=3)
print(a)

#dtype parameter.
import numpy as np
a=np.array([1,2,3,4,5],dtype=float)
print(a)

#using array scalar type.
import numpy as np
dt=np.dtype(np.int64)
print(dt)

##int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc. 
import numpy as np 
dt=np.dtype('i2')
print(dt)

## first create structured data type
import numpy as np
dt=np.dtype([('age',np.int32)])
print(dt)

#apply to ndarray objects.
import numpy as np
dt=np.dtype([('age',np.int8)])
a=np.array([(10,),(20,),(30,)],dtype=dt)
print(a)

#creating the dtype of student.
import numpy as np
student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)

import numpy as np
student=np.dtype([('name','S10'),('age','i1'),('marks','c')])
a=np.array([('Hitesh',27,76),('Rahul',28,68)],dtype=student)
print(a)

#ndarray.shape.return array dimention and total number of attributes. .
import numpy as np
a=np.array([[1,2,3,10],[20,30,50,60]])
print(a.shape)

#resize the ndarray.
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
a.shape=(3,2)
print(a)

#reshape function.
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(3,2)
print(b)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(1,6)
print(b)


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(6,1)
print(b)

#ndim returns the array dimentions.
import numpy as np
a=np.arange(24)
print(a)
print(a.ndim)

#ndim returns the array dimentions.
import numpy as np
a=np.arange(24)
print(a)
print(a.ndim)

#rshape the array list.
b=a.reshape(2,4,3)
print(b)

#numpy.itemsize it returns the length of each elements of the array.
import numpy as np
x=np.array([1,2,3,4,5],dtype=np.int32)
print(x.itemsize)

import numpy as np
x=np.array([1,2,3,4,5],dtype=np.complex)
print(x.itemsize)

#numpy.flag it will return the current values of flag.
import numpy as np
x=np.array([1,2,3,4,5])
print(x.flags)

#numpy.empty it gives you uninitialised array with specified shape and dtype.
import numpy as np
x=np.empty([4,4],dtype=int)
print(x)

#numpy.zeros it will return array with specified size with zeros.
import numpy as np
x=np.zeros(5)
print(x)

import numpy as np
x=np.zeros((5),dtype=np.int)
print(x)

import numpy as np
x=np.zeros((2,2),dtype=int)
print(x)

import numpy as np
x=np.zeros((2,2))
print(x)

#numpy.zeros it will return array with specified size with once.
import numpy as np
x=np.ones(5)
print(x)

x=np.ones((5),dtype=int)
print(x)

x=np.ones((2,2),dtype=int)
print(x)

#Arange function.which return the ndarray object containing the value in the list.
import numpy as np
x=np.arange(5)
print(x)


import numpy as np
x=np.arange(5,dtype=float)
print(x)

#poviding the start,stop and space betwwen th list.
import numpy as np
x=np.arange(10,20,2)
print(x)

#linspace function same as the arange function.
import numpy as np
x=np.linspace(10,20,5)
print(x)

import numpy as np
x=np.linspace(10,20,5,endpoint=False)
print(x)

import numpy as np
#printing one dimentional array.
a=np.array([1,2,3,4,5])#array contains one rows.
print(a)
#checking the dimention of array.
print(a.ndim)
#checking the data type of elements.
print(a.dtype)
#Sum of all element in array.
print(a.sum())
#Min element from array.
print(a.min())
#Max element from array.
print(a.max())

np.arange(10,20,3)
np.linspace(1,10,20)



import numpy as np
#printing two dimentional array.
b=np.array([[1,2],[3,4],[5,6]])#Contains three rows and two columns.
print(b)
#checking the dimention of array.
print(b.ndim)
#checking the data type of elements.
print(b.dtype)

print(b.sum())
print(b.min())
print(b.max())

b.sum(axis=0)#It's gives column wise addition of matrix.
b.sum(axis=1)#It's gives row wise aditon of matraix.


import numpy as np
#printing the three dimemntional array.
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]],dtype=np.float64)#two dimention ,two rows and two columns.
print(c)
print(c.ndim)
#checking the data type of elements.
print(c.dtype)

print(c.sum())
c.sum(axis=0)
c.sum(axis=1)

































































































