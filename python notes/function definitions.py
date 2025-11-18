#FUNCTION DEFINITIONS
#what if we dont know the order of the arguments to be passed but the names of the parameter
def pow(x,y):
    print(x**y)
#we can call it like
pow(y=2,x=4)#for 4 power 2
#DEFAULT VALUE SETTING
#if we set a default value to the fuction, it does not executed dynamically

#but if define the l first
l=[1,2,3,4,5,6,7,8]
def printList(l,length=len(l)):
    for i in range(length):
        print(i,end=' ')
printList(l)
print()
print("the next functions list(1 to 4)")
printList([1,2,3,4])
print()
#def printlist(L,length=len(L)):#you can see the red line under l, which shows
 #   pass                       #us that it will not take the first argument
                               #for the evaluation of len()
#assingnment of function name to other
lister=printList
print('the lister function')
lister(l)
print()
#practical usage of this 
print('multiplying functions')
def multiply(x,y=2):
    print(x*y)
def multiply_times(multiplier,z,times=2):#assigning the multiply fuction to multiplier
    for i in range(times):
        multiplier(z)
multiply_times(multiply,10)
