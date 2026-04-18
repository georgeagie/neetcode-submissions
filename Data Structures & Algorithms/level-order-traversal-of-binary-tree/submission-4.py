# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            level = []
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

            if level:
                levels.append(level)

        return levels
        