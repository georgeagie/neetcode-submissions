# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        to_remove = dummy
        advanced = head
        for i in range(n):
            advanced = advanced.next
        while advanced:
            to_remove = to_remove.next
            advanced = advanced.next
        to_remove.next = to_remove.next.next
        return dummy.next