class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = -1
        while digits[i] == 10:
            digits[i] = 0
            if i * -1 == len(digits):
                digits.insert(0, 1)
            else:
                digits[i - 1] += 1
            i -= 1
        return digits