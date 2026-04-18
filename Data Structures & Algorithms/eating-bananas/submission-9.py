class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        min_k = r

        while l <= r:
            time = 0
            k = (l + r) // 2

            for pile in piles:
                time += math.ceil(pile / k)

            if time > h:
                l = k + 1
            else:
                min_k = min(min_k, k)
                r = k - 1

        return min_k

            