class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0

        for i in elements:
            if (i - 1) not in elements:
                length = 1
                while (i + length) in elements:
                    length += 1
                longest = max(length, longest)
        return longest