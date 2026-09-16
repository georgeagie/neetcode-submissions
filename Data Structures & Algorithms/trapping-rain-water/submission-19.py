class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = 0
        r_max = 0
        total = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if height[l] < height[r]:
                total += max(min(l_max, r_max) - height[l], 0)
                l += 1
            else:
                total += max(min(l_max, r_max) - height[r], 0)
                r -= 1

        return total