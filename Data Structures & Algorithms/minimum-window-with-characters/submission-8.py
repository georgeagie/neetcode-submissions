class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = 0
        r = 0
        min_window = 999999
        res = ""

        t_map = {}
        for i in range(len(t)):
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        print(t_map)
        while r < len(s):
            s_map = {}
            for i in range(r - l + 1):
                if s[i + l] in t_map.keys():
                    if s_map.get(s[i + l], 0) < t_map[s[i + l]]:
                        s_map[s[i + l]] = 1 + s_map.get(s[i + l], 0)
            print(s_map)

            if s_map == t_map:
                if r - l + 1 < min_window:
                    min_window = r - l + 1
                    res = s[l:r + 1]
                    print(res)
                l += 1
            else:
                r += 1
            
        
        return res

