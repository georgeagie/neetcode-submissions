class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_length = 0

        seen = {}
        while end < len(s):
            c = s[end]
            if c in seen.keys():
                idx_to_remove = seen[c]
                while start <= idx_to_remove:
                    del seen[s[start]]
                    start += 1
            else:
                seen[c] = end
                end += 1
                max_length = max(max_length, len(seen))
        
        return max_length