# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        
        res = ListNode()
        curr_res = res

        while curr1 or curr2:
            curr1_val = curr1.val if curr1 else 0
            curr2_val = curr2.val if curr2 else 0
            curr_sum = curr1_val + curr2_val + curr_res.val

            carry_over = 0
            if curr_sum > 9:
                curr_res.val = curr_sum % 10
                carry_over = 1
            else:
                curr_res.val = curr_sum
            
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            if not curr1 and not curr2 and not carry_over:
                break
            curr_res.next = ListNode(val = carry_over)
            curr_res = curr_res.next

        return res