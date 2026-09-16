class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s2) < k:
            return False
        s1_map = {}
        window = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        for i in range(k):
            window[s2[i]] = window.get(s2[i], 0) + 1
        if window == s1_map:
            return True
        for i in range(k, len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1
            left_char = s2[i - k]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == s1_map:
                return True
        return False