#the any function takes one argument that is an iterable, it iterates through the passed\
#iterable and returns True if there is ATLEAST one True. it returns False only if all the elements of the iterable is False.
print(any([1,2,3,4,6,0]))#returns True as there is True values in the iterable
print(any([0,1,0,0]))
print(any([0,0,0]))#returns false as there is no True values in the iterable
