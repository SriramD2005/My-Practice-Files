def quicksort(list):
    if len(list)<1:
        return list
    pivot=list[0]
    left=[x for x in list if x<pivot]
    right=[x for x in list[1:] if x>=pivot]
    return quicksort(left)+[pivot]+quicksort(right)
print(quicksort([7,3,5,9,1]))
