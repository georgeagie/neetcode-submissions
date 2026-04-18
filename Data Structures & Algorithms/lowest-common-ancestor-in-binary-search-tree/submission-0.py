# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr != None:
            if p.val < curr.val:
                if q.val < curr.val:
                    curr = curr.left
                else: 
                    return curr
            elif p.val > curr.val:
                if q.val > curr.val:
                    curr = curr.right
                else:
                    return curr
            else:
                return curr

        return curr
            
            