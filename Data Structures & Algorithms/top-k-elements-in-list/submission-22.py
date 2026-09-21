import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq_map = {}
        # for num in nums:
        #     freq_map[num] = 1 + freq_map.get(num, 0)
        
        # min_heap = []
        # for num, freq in freq_map.items():
        #     heapq.heappush(min_heap, (freq, num))
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        
        # result = []
        # for i in range(k):
        #     result.append(heapq.heappop(min_heap)[1])
        # return result
        
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            while len(buckets[i]) > 0:
                if k > 0:
                    result.append(buckets[i].pop())
                    k -= 1
                else:
                    return result

        return result

            