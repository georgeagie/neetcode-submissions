class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        stack = []

        for i, height in enumerate(heights):
            if stack:
                if height > stack[-1][0]:
                    stack.append((height, i))
                else:
                    last_popped = stack[-1][-1]
                    while height <= stack[-1][0]:
                        popped_height, popped_index = stack.pop(-1)
                        area = popped_height * (i - popped_index)
                        max_area = max(max_area, area)
                        last_popped = popped_index
                        if len(stack) == 0:
                            break
                    stack.append((height, last_popped))
            else:
                stack.append((height, i))
        
        while stack:
            popped_height, popped_index = stack.pop(-1)
            area = popped_height * (len(heights) - popped_index)
            max_area = max(max_area, area)
        
        return max_area
        