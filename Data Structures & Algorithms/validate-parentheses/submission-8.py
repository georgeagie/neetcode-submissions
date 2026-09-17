class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        stack = []
        for c in s:
            if c in hm.keys():
                stack.append(c)
            else:
                if not stack or hm[stack.pop()] != c:
                    return False
        
        return True if len(stack) == 0 else False