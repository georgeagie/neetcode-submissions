# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isSameTree(curr, sub):
            if not sub and not curr:
                return True
            elif (not curr and sub) or (curr and not sub):
                return False
            
            if curr.val != sub.val:
                return False
            else:
                return isSameTree(curr.left, sub.left) and isSameTree(curr.right, sub.right)

        if root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)