x=2
#assert (x==3) ,"x is not equal to 3"
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
try:
    divide(3,0)
except ZeroDivisionError:
    raise
#if you give raise statement alone it will reraise the already active error