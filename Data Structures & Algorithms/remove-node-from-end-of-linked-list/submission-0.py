# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = head
        counter = 1
        while x.next:
            counter += 1
            x = x.next
        a = head
        if n == counter:
            return head.next
        for _ in range(counter - n - 1):
            a = a.next
        a.next = a.next.next
        return head


        
