class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            else:
                curr_length = 1
                while num + curr_length in nums_set:
                    curr_length += 1
                max_length = max(max_length, curr_length)

        return max_length