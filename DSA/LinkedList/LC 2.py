class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        c1,c2=l1,l2
        resnode=ListNode()
        c3=resnode
        while(c1 and c2):
            r=(l1.val+l2.val)%10
            c3.val=r
            c1=c1.next
            c2=c2.next
            c3.next=ListNode()
            c3=c3.next
        if (c1):
            c1.val+=r
            c3.next=c1
        if (c2):
            c2.val+=r
            c3.next=c2
        return resnode
        


