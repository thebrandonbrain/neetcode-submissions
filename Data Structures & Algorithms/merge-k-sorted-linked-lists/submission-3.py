class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def mergeTwoLists(list1, list2):
            dummy = ListNode(0)
            curr = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next

                curr = curr.next

            if list1:
                curr.next = list1
            else:
                curr.next = list2

            return dummy.next
        while len(lists) > 1:
            dnc = []
            for i in range(0, len(lists), 2):
                if i < len(lists) - 1:
                    dnc.append(mergeTwoLists(lists[i], lists[i+1]))
                else:
                    dnc.append(lists[i])
            lists = dnc
        return lists[0]