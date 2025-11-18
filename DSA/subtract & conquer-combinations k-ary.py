#finding combinations for n places with k domain={0,1,...,k-1}
def getdomain(k):
    return [str(x) for x in range(k)]
def comb(n,k):
    domain=getdomain(k)
    if n==1:
        return domain
    return [i+j for i in domain for j in comb(n-1,k)]
print(comb(2,4))