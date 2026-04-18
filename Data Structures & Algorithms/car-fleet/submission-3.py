class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        
        pos_speed.sort(reverse=True)

        stack = []
        num_fleets = 1

        for p, s in pos_speed:
            time = (target - p) / s
            if stack:
                if time > stack[-1]:
                    stack.append(time)
                    num_fleets += 1
            else:
                stack.append(time)
        
        return num_fleets