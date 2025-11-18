def insertion(list):
    for pos in range(1,len(list)):
        currentval=list[pos]
        while pos>0 and currentval<list[pos-1]:
            list[pos]=list[pos-1]
            pos-=1
        list[pos]=currentval
    print(list)
insertion([i for i in range(2000,0,-1)])



