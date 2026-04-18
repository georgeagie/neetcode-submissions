class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm.keys():
                return list([hm.get(nums[i]), i])

            hm[target - nums[i]] = i

        return null