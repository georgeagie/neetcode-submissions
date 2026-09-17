class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_indices = []
        t_map = {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
        need = len(t_map.keys())
        have = 0
        l = 0
        window = {}
        for r in range(len(s)):
            if s[r] in t_map.keys():
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == t_map[s[r]]:
                    have += 1
            while have == need:
                if len(min_indices) == 0 or (r - l) < (min_indices[1] - min_indices[0]):
                    min_indices = [l, r]
                if s[l] in window.keys():
                    window[s[l]] -= 1
                    if window[s[l]] < t_map[s[l]]:
                        have -= 1
                l += 1
        if len(min_indices) == 0:
            return "" 
        return s[min_indices[0]:min_indices[1] + 1]

            