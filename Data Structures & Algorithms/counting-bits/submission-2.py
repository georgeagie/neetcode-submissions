class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for x in range (n + 1):
            count = 0
            mask = 1
            for i in range(32):
                count += (x >> i) & mask
            result.append(count)

        return result