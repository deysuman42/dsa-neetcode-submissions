class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_ = {}
        for i in nums:
            if i in hash_:
                return True
            else:
                hash_[i] = 1 + hash_.get(i, 0)
        return False
        