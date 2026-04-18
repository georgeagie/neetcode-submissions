class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return [max(nums)] * len(nums)

        res = [-999999] * (len(nums) - k + 1) 

        l = 0
        r = k - 1

        

        while r < len(nums):
            res[l] = max(nums[l:r + 1])
            l += 1
            r += 1

        return res
