class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        s1_map = {}

        for i in range(len(s1)):
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)
        print(s1_map)

        while r < len(s2):
            s2_map = {}
            for i in range(r - l + 1):
                s2_map[s2[i + l]] = 1 +  s2_map.get(s2[i + l], 0)
            print(s2_map)
            if s1_map == s2_map:
                return True

            l += 1
            r += 1

        return False