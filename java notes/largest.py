a,b,c=10,5,40
def ma(a,b,c):
    if a>b:
        if b>c:
            return (a)
        else:
           return c if c>a else a
    else:
        if a>c:
            return b
        else:
            return c if c>b else b
print(ma(a,b,c))
        
    