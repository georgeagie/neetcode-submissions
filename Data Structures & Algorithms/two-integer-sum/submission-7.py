class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_idx = {}

        for i in range(len(nums)):
            if nums[i] in comp_idx.keys():
                return [comp_idx[nums[i]], i]
            comp_idx[target - nums[i]] = i
        
        return null