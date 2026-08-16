class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        array_index = [[] for i in range(0, len(nums) + 1)] 

        # hover through 
        for num, v in freq.items():
            array_index[v].append(num)
        for i in range(len(array_index) -1, 0, -1):
            for num in array_index[i]:
                res.append(num)
                if len(res) == k:
                    return res