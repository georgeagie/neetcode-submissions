class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            target = -1 * nums[i]
            while l < r:
                curr = nums[l] + nums[r]
                if curr > target:
                    r -= 1
                elif curr < target:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
            
    
        return res