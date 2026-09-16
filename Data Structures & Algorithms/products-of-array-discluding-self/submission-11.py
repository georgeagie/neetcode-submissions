class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        current = 1
        for i in range(len(nums)):
            res[i] *= current
            current *= nums[i]
        current = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= current
            current *= nums[i]
        return res