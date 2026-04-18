class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = ""
        for c in s:
            if c.isalnum():
                s_filtered += c

        for i in range(len(s_filtered)//2):
            front = s_filtered[i].lower()
            end = s_filtered[-1*(i + 1)].lower()
            if front != end:
                return False
        
        return True