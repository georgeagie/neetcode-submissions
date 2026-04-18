class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                count[i] += 1
            
            hm[tuple(count)].append(s)

        return list(hm.values())