class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for day, temperature in enumerate(temperatures):
            while stack:
                if temperature > stack[-1][0]:
                    _, index = stack.pop(-1)
                    res[index] = day - index
                else: 
                    break
            stack.append((temperature, day))
        
        print(res)
        return res