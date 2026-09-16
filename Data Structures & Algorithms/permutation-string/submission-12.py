class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l = 0
        r = len(s1) - 1
        s1_map = {}
        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)
        while r < len(s2):
            if self.is_anagram(s1_map, s2[l:r + 1]):
                return True
            l += 1
            r += 1
        return False

    def is_anagram(self, s1_map, s2):
        print(f"{s1_map}, {s2}")
        s2_map = {}
        for c in s2:
            s2_map[c] = 1 + s2_map.get(c, 0)
        return s1_map == s2_map
