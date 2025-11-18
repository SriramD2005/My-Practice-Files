# coding: utf-8
import numpy as np
# usage of np.newaxis keyword
#this keyword is used to transform a one dimensional array to two dimensional row or column vector
x = arange(3)
x = np.arange(3)
x
x[:, np.newaxis]
x[1, np.newaxis]
x[2, np.newaxis]
#this is for column vector, for row vector:
x[np.newaxis, :]
