from pendingInsertion import *
addNode(list, Node(24))
l1 = Node(1)
l2 = Node(9)
for i in range(2, 5):
    addNode(l1, Node(i))
for i in range(3, 6):
    addNode(l2, Node(i))
merge = Node(99)
addNode(l2, merge)
addNode(l1, merge)
curr = merge
for i in range(20, 25):
    new = Node(i)
    curr.next = new
    curr = new
#by HASH MAP  Time Complexity: O(m + n) Space Complexity: O(max(m, n))
#we put the list with bigger size in the hash map to reduce the time complexity of searching
def byHashmap(l1, l2):
    intersection = {}
    curr = l1
    while curr:
        intersection[curr] = True
        curr = curr.next
    curr = l2
    while curr:
        if intersection.get(curr):
            print(curr.value)
            break
        curr = curr.next
#by SORTING TECHNIQUE Time Complexity: O(max(nlogn, mlogm)) Space Complexity: O(max(m + n))
def bySortingTech(l1, l2):
    curr = l1
    fl, sl = [], []
    while (curr):
        fl.append(curr)
        curr = curr.next
    curr = l2
    while (curr):
        sl.append(curr)
        curr = curr.next
    fl.sort(key = lambda x : id(x))
    sl.sort(key = lambda x : id(x))
    for fptr in fl:
        left = 0
        right = len(sl)
        while left < right:
            mid = (left + right)//2
            if id(fptr) == id(sl[mid]):
                return fptr.value
            if id(fptr) < id(sl[mid]):
                right = mid
            if id(fptr) > id(sl[mid]):
                left = mid
#by USING STACK
def byStack(l1, l2):
    stack1, stack2 = [], []
    curr = l1
    while (curr):
        stack1.append(curr)
        curr = curr.next
    curr = l2
    while (curr):
        stack2.append(curr)
        curr = curr.next
    #print(stack1, stack2, end = '\n')
    prev = 0
    while stack1 and stack2:
        element = stack1.pop()
        if id(element) == id(stack2.pop()):
            prev = element
            continue
        return prev.value
#USING TWO POINTERS
def twoPointers(l1, l2):
    p1 = l1
    p2 = l2
    while p1 and p2 and id(p1) != id(p2):
        p1 = p1.next
        p2 = p2. next
    return p1.value
print(twoPointers(l1, l2))