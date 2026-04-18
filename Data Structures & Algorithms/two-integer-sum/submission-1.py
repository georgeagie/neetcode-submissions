class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        h_map ={}
        for i, n in enumerate(nums):
            if target - n in h_map:
                return [h_map[target - n], i]
            h_map[n] = i