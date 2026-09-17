class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top < bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid
        # must be in top/bottom since they match
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[top][mid] < target:
                l = mid + 1
            elif matrix[top][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False