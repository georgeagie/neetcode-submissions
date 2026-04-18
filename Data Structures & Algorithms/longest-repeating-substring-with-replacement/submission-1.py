class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = max_length = 0

        for r in range(len(s)):
            freq = {}
            for i in range(r - l + 1):
                freq[s[i + l]] = 1 + freq.get(s[i + l], 0)
            
            max_freq = 0
            for count in freq.values():
                max_freq = max(max_freq, count)
            
            if r - l + 1 - max_freq <= k:
                max_length = max(max_length, r - l + 1)
            else: 
                l += 1
        
        return max_length