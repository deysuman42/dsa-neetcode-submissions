class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Two Pointer
        m = 0
        n = 1
        min_value = nums[m]

        while n <= len(nums) - 1:
            if nums[n] < nums[m]:
                min_value = nums[n]
                m = n
            n += 1
        return min_value
            


        