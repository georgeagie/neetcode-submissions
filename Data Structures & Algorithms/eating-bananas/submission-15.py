class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_k = high
        while low <= high:
            hours = 0
            k = low + (high - low) // 2
            for pile in piles:
                hours += (pile + k - 1) // k
            print(k)
            print(hours)
            if hours > h:
                low = k + 1
            else:
                min_k = min(min_k, k)
                high = k - 1

        return min_k