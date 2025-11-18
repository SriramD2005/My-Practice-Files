from c3p31 import *
def mergeList(l1, l2):
    dummy = Node(-1)
    p3 = dummy

    while l1 and l2:
        if l1.value < l2.value:
            p3.next = l1
            l1 = l1.next
        else:
            p3.next = l2
            l2 = l2.next
        p3 = p3.next

    p3.next = l1 if l1 else l2
    return dummy.next
printList(mergeList(l1, l2))