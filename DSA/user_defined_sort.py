#user defined sort
nlist=[]
while True:
    x=input('Your input:')
    if x=='order it':
        break
    nlist.append(x)
print("name list that you have entered:",nlist)
list1=[]
for i in nlist:
    list1.append(list(i))
def user_defined_sort(L):
    def swap(l,i,j):
        x=l.index(i)
        y=l.index(j)
        l[x],l[y]=l[y],l[x]
    for i in L:
        count=0
        n=[]
        for j in L:
            count=0
            if len(i)<len(j):
                n=list(range(len(i)))
            elif len(j)<len(i):
                n=list(range(len(j)))
            elif len(j)==len(i):
                n=list(range(len(j)))
            if L.index(i)>L.index(j):
                for l in range(0,len(n)):
                
                    if i[l]==j[l]:
                        count+=1
                    
                    if count!=l+1:#one is small L and another is 1
                        if i[l]<j[l]:
                            swap(L,i,j)
                        elif i[l]>j[l]:
                            pass
                        break
                    if count==len(n):
                        if len(i)<len(n):
                            swap(L,i,j)
            else:
            
                for l in range(0,len(n)):
                    if i[l]==j[l]:
                        count+=1
                        
                    if count!=l+1:#one is small L and another is 1
                        if i[l]>j[l]:
                            swap(L,i,j)
                        elif i[l]<j[l]:
                            pass
                        break
                    if count==len(n):
                        if len(i)>len(n):
                            swap(L,i,j)
    L1=[]
    for i in L:
        sum=i[0]
        for j in range(1,len(i)):
            sum+=i[j]
        L1.append(sum)
    print(L1)
user_defined_sort(list1)
 

                
                
                

        
            
            

            
        
    



    
