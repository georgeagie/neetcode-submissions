class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0

        total_water = 0

        while l <= r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            
            moved_left = True
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
                moved_left = False

            
            if moved_left:
                if height[l - 1] < min(l_max, r_max):
                    total_water += min(l_max, r_max) - height[l - 1]
            else:
                if height[r + 1] < min(l_max, r_max):
                    total_water += min(l_max, r_max) - height[r + 1]

        return total_water