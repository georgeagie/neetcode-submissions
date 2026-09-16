class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                max_length = max(max_length, len(seen))
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
        return max_length