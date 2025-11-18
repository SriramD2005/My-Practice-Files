numbers=[1,2,3,4,5]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        numbers[i]=-99
res=[x for x in numbers if x!=-99]
numbers=res
print(numbers)
