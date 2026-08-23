class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        position_target = []
        n = len(position)
        for i in range(n):
            val = (target - position[i]) / (speed[i])
            position_target.append((position[i], val))
        position_target.sort(reverse = True)
        
        for i in position_target:
            if not res:
                res.append(i[1])
            else:
                if res[-1] < i[1]:
                    res.append(i[1])
        return len(res)