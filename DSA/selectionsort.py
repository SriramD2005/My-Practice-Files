list=[5,1,3,8,4]
for i in range(len(list)):
    min=i
    for j in range(i+1,len(list)):
        if list[min]>list[j]:
            list[min],list[j]=list[j],list[min]
print(list)