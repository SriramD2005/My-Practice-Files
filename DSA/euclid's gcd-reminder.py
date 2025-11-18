def euclid(m,n):
    if m%n==0:
        print(n)
    else:
        euclid(n,m%n)
euclid(24,15)