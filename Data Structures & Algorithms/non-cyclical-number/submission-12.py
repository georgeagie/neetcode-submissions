class Solution:
    def sumOfSquares(self, x: int) -> int:
        x = str(x)
        total = 0
        for c in x:
            total += (ord(c) - ord('0')) ** 2
        return total

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
            print(n)
            if n == 1:
                return True
        return False
