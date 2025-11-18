#In Python, all the datatypes are pass-by-value(of reference), all the datatypes are object
#If a datatype is immutable, then the compiler cannot change it by in place, so it creates a new local variable
#and assigns it to the parameter passed.
# Example 
def fun(a):
    a = 99
    print("in function", a)
a = 2
fun(a)
print(a)
#but the immutables can change the value in inplace so we can do inplace modifications of passed object, but
#we cannot reassign it, as this creates a new local object, actually we can reassign but it will change from global to local
#Example
def inplaceSort(l):
    l.sort()
def returnSort(l):
    l = sorted(l)
l = [3,5,1,4]
print("list:", l)
returnSort(l)
print("after returnSort",l)
inplaceSort(l)
print("after inplaceSort", l)
