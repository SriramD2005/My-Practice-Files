# coding: utf-8
import numpy as np
#In python(default CPython interpreter), the loops in python are very slow, for example:
def reciprocal(lst):
    result=[]
    for i in lst:
        result+=1/i
    return result
del In[3]
#the slowness is due to the dynamically typed nature of the variables, for each loop, the type of the variable must be determined and the operator corresponding to it must be selected for each loop, the operation itself doesn't causes late.
#the solution is to "vectorize"(converting to matrix form) the operation that are to be repeated many times. By this we predefine the type(as numpy is homogeneous) and fixing the operator to be used. there by we are making a compiled layer. the compiler in compiled languages does this, like predefining the variable type and operator.r
get_ipython().run_line_magic('timeit', '1/x')
x=np.arange(1,1000000)
get_ipython().run_line_magic('timeit', 'reciprocal(list(range(1,1000000)))')
