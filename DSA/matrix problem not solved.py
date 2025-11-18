def leftrotate(m):
    x=[[]]*len(m)
    print(x)
    for i in range(len(x)):
        print('hi')
        
        for j in range(len(x)):
            print(m[j][len(m)-i-1])
            print(i)
            x[i].append(m[j][len(m)-i-1])
            print(x[i])
    print(x)
leftrotate([[2,3],[4,5]])

