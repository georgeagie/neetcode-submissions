class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s2) < k:
            return False
        s1_map = {}
        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)
        window = {}
        for i in range(k):
            window[s2[i]] = 1 + window.get(s2[i], 0)
        if window == s1_map:
            return True
        for i in range(k, len(s2)):
            window[s2[i]] = 1 + window.get(s2[i], 0)
            window[s2[i - k]] -= 1
            if window[s2[i - k]] == 0:
                del window[s2[i - k]]
            if window == s1_map:
                return True
        return False