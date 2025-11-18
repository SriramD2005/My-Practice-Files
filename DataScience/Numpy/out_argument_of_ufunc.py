# coding: utf-8
#memory saving using the out argument of all the UFunctions.
import numpy as np
y=np.empty(10)
x=np.arange(1,1000000)
#if we use normal assignment to store the values in the y after performing some UFunctions in x, it temporarily creates an array that is applied with UFunctions and copies those values into y.
y=2**x
#this first creates an array, that is temporary and stores the values that are 2**x
#then it copies the values to the y 
#but if we use the 'out' argument of the UFunctions, we can directly write into the memory location of y
np.pow(2,x,out=y)
