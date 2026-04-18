# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        q.append(root)

        while q:
            rightSide = None
            level_length = len(q)
            for i in range(level_length):
                curr = q.popleft()
                if curr:
                    rightSide = curr
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            
            if rightSide:
                res.append(rightSide.val)
        
        return res