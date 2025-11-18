from LinkedList import *
l1 = Node(1)
l2 = Node (5)
l3 = Node(0)
for i in range(2, 10, 2):
    addNode(l1, Node(i))
addNode(l1,Node(0))
addNode(l1, Node(3))
for i in range(1, 10, 3):
    addNode(l2, Node(i))
addNode(l2, Node(2))
printList(l1)
printList(l2)
class addLists:
    def __init__(this, l1, l2, carry = 0):
        this.l1 = l1
        this.l2 = l2
        this.l3 = Node(-99)
        this.carry = carry
    def addNodes(this, fp, sp, tp):
        third = Node(-99)
        tp.next = third
        if fp.next and sp.next:
            this.addNodes(fp.next, sp.next, tp.next)
        else:
            if fp.next:
                this.addNodes(fp.next, sp, tp.next)
            if sp.next:
                this.addNodes(fp, sp.next, tp.next)
        if fp is this.l1 and sp is this.l2:
            sum = fp.value + sp.value + this.carry
            this.carry = sum // 10
            digit = sum % 10
            tp.value = digit
            if not this.carry:
                temp = tp
                tp = Node(this.carry)
                tp.next = temp
        else:
            if fp is this.l1:
                sum = fp.value + this.carry
                this.carry = sum // 10
                digit = sum % 10
                tp.value = digit
            elif sp is this.l2:
                sum = sp.value + this.carry
                this.carry = sum // 10
                digit = sum % 10
                tp.value = digit
            else:
                print("last recursion:", )
                sum = sp.value + this.carry
                this.carry = sum // 10
                digit = sum % 10
                tp.value = digit
    def getSumList(this):
        this.addNodes(this.l1, this.l2, this.l3)
        return this.l3
add = addLists(l1, l2)
printList(add.getSumList())