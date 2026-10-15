class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            rate = left + ((right - left) // 2)
            hours = 0
            for i in piles:
                hours += math.ceil(i / rate)
            if hours <= h:
                res = min(res, rate)
                right = rate - 1
            else:
                left = rate + 1
        return res

        