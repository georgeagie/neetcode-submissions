class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = 9999999
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            minimum = min(nums[mid], minimum)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return minimum