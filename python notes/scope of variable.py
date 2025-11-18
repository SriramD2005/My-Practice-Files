#SCOPE OF VARIABLE
x=3

def func():
    y=x
    print(y)
func()
#this code do not throws an error because the fuction first searches the variable in its namespace
#then it searches the global.
#IF THE FUNC IS CHANGED LIKE THIS
def func():
    #y=x
    #print(y)
    x=2
func()
#this throws a unbound error(not name error) because the x is available in the namespace of the function, so it does not 
#search outside it. but why it is showing error? even though the value is available in namespace, it
#it is called before its assignment.
#BUT WHAT IF IT IS "MUTABLE DATA TYPE"?
x=[1,2,3]
def func():
    y=x[2]
    print(y)
    x[2]=5
func()
#this does not throws an error because we did not reassign the value of the variable, which creates
#a new variable, we just modifying the mapping of the index, but the x variable still pointing the 
#same memory address
