class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # rotated by multiples of length of nums
        if nums[0] < nums[-1]:
            return nums[0]

        while left < right:
            mid = left + ((right - left) // 2)

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


        