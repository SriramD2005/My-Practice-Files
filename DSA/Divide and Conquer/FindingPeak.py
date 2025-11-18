def findpeak(arr):
    if len(arr) == 1:
        return arr[0]
    mid = (len(arr) - 1)//2
    #print(mid)
    left = arr[mid - 1] if mid != 0 else -float("inf")
    right = arr[mid + 1] if mid != len(arr) - 1 else float("inf")
    if arr[mid] >= left and arr[mid] >= right:
        return arr[mid]
    else:
        if arr[mid] < right:
            return findpeak(arr[mid+1:])
        else:
            return findpeak(arr[:mid])
print(findpeak([1,2,3,4,5,1,10,4,5]))