class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        print(count)
        freq = []
        for i in range(len(nums)):
            freq.append([])
        print(freq)

        for n, c in count.items():
            freq[c - 1].append(n)
        print(freq)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]: # Loop through the numbers in this specific bucket
                res.append(n)
                if len(res) == k:
                    return res