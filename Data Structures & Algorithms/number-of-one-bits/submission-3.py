class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1
        for i in range(32):
            count += (n >> i) & mask
        
        return count