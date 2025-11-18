def fun(*a):
    x = 1
    for i in a:
        x *= i
    return x
print(fun(2,3,4))