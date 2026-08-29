import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        minpiles = min(piles)
        maxpiles = max(piles)
        
        left = 1
        right = max(piles) + 1

        while left < right:
            mid = left + ((right - left) // 2)
            s = 0
            for i in piles:
                s += math.ceil((i / mid))
            if s > h :
                left = mid + 1
            else:
                right = mid
        return left

            