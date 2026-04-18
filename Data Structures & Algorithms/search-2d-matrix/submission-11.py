class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                l = 0
                r = len(matrix[0]) - 1

                while l <= r:
                    m = (l + r) // 2

                    if matrix[mid][m] > target:
                        r = m - 1
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        return True
                
                return False
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        
        return False
