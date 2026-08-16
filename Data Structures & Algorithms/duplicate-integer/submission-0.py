class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        h = {}
        for i in nums:
            print(h)
            if i not in h:
                h[i] = 1
            else:
                return True
        return False