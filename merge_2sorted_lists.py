from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        l = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                l.next = list1.val
                list1 = list1.next
            else:
                l.next = list2.val
                list2 = list2.next
            # l.next = ListNode()
            l = l.next
        if list1:
            l.next = list1
        else:
            l.next = list2
        return dummy.next
