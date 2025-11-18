def euclid(m,n):
    if m%n==0:
        print(n)
    elif n%m==0:
        print(m)
    else:
        euclid(((m-n)**2)**0.5,n)
euclid(24,16)
