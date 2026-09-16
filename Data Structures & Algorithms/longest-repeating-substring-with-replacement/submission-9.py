class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        l = 0
        freq_map = {}
        max_f = 0
        for r in range(len(s)):
            freq_map[s[r]] = 1 + freq_map.get(s[r], 0)
            max_f = max(max_f, freq_map[s[r]])
            while (r - l + 1) - max_f > k:
                freq_map[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length

            

