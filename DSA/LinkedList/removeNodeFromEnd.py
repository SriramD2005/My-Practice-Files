# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#INEFFICIENT - TWO PASS
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        till = length - n 
        print(till)
        if (length <= 1):
            return None
        if (till == 0):
            return head.next
        count = 0
        curr = head
        while curr:
            count += 1
            if count == till:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
#EFFICIENT - ONE PASS (USING TWO POINTERS)
class OnePass:
    def removeNthFromEnd(head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next