class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {'(':')', '[':']', '{':'}'}

        for c in s:
            if c in brackets.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or brackets[stack[-1]] != c:
                    return False
                stack.pop()
        
        return len(stack) == 0