#reverse K blocks in linked list
#input: k:3 list:1,2,3,4,5,6,7,8
#output:3,2,1,6,5,4,7,8
from LinkedList import *
printList(l)
def reverseKBlocks(l, k):
    start = l
    end = start
    while end:
        for i in range(k-1):
            end = end.next
            if not end:
                return l
        actualend = end
        reverse(start, end)
        start = actualend.next
        end = start
def reverse(start, end):
    curr = start
    