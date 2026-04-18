class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        one = 1
        two = 1
        res = 0

        for i in range(n - 1):
            res = one + two
            temp = one
            one = res
            two = temp

        return res