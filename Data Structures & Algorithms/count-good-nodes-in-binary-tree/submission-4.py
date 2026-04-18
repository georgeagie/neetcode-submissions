# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, curr_max):
            if not curr:
                return 0
            is_good = 0
            if curr.val >= curr_max:
                is_good = 1
            print(f"curr: {curr.val}")
            print(f"curr_max: {curr_max}")
            print(f"is_good: {is_good}")
            
            curr_max = max(curr_max, curr.val)
            
            return is_good + dfs(curr.left, curr_max) + dfs(curr.right, curr_max)


        return dfs(root, float("-inf"))
         