class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums))]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c - 1].append(n)

        res = []

        for i in range (len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                k -= 1
                if k == 0: 
                    return res

        return res