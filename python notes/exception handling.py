#EXCEPTION HANDLING
#Like in loops the else block will excute only if the try block is executed
#without except block 
x=int(input('x:'),16)
try:
    print(x/x,x)
except ZeroDivisionError:
    print('no else block')
else:
    print('as except block didnt worked else is working')
