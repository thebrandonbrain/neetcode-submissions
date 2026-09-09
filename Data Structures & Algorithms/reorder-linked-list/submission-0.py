# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        slow = slow.next
        curr.next = None
        l1 = head
        l2 = slow
        prev = None
        while l2:
            ptr = l2.next
            l2.next = prev
            prev = l2
            l2 = ptr
        l2 = prev
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
        l1 = head