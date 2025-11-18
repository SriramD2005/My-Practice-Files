from math import log
def recursive_log2n(n):
    if n<1:
        return -1
    return 1+recursive_log2n(n/2)
def non_recursive_log2(n):
    return log(n,2)
print(non_recursive_log2(8))
def non_recursive_printrange(start,end):
    print('non recursive range',end=' ')
    for i in range(start,end+1):
        print(i,end=' ')
    print()
def recursive_printrange(start,end):
    if start>end:
        return 
    print(start)
    recursive_printrange(start+1,end)
non_recursive_log2(8)
print(recursive_log2n(4))       
recursive_printrange(2,8)
non_recursive_printrange(3,8)