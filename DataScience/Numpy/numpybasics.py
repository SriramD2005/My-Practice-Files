# coding: utf-8
import numpy as np
x=np.array([1,2,3],dtype=np.float32)
#float32 is a numpy numpy object
#or
x=np.array([1,2,3],dtype="float32")
np.ones((3,4))
np.zeroes((2,3))
np.zeros((2,3))
np.end((2,3))
np.empty((2,3))
#the empty returns whatever there in that memory location for the given shape
#In random module of numpy, to get every the same random as we run the code we use
np.random.seed(0)
#so every time when we run the code the random generates the same random value as it was ran first
#the item size attribute of the numpy array gives the size of the each item stored in the array(numpy array is homogeneous)
x.itemsize
x.nbytes
#
#example:
x_slice=x[:1]
x_slice[0]=99
x
#in python default list the slicing returns a copy of the list, we cant do any inplace operations with that copy. But in numphy the slices returns the inplace pointers any changes done in the sliced variables will reflect in the original array. To get the copy use the copy method of array object
x_slice=x[:1].copy()
x_slice[0]=0
x
x_slice
x,x_slice
