"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new = {None : None}
        
        cur = head

        while cur:
            copy = Node(cur.val)
            old_new[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = old_new[cur]
            copy.next = old_new[cur.next]
            copy.random = old_new[cur.random]
            cur = cur.next
        
        return old_new[head]
