class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Two Pointer
        # m = 0
        # n = 1
        # min_value = nums[m]

        # while n <= len(nums) - 1:
        #     if nums[n] < nums[m]:
        #         min_value = nums[n]
        #         m = n
        #     n += 1
        # return min_value


        left = 0
        right = len(nums) - 1
        res = nums[0]

        while left <= right:

            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break;

            m = left + (right - left) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1
        return res



            

        


            


        