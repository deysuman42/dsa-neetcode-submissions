class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap_s = {}
        res = float('-inf')
        l = 0
        maxf = 0

        for r in range(len(s)):
            hashmap_s[s[r]] = 1 + hashmap_s.get(s[r], 0)
            maxf = max(maxf, hashmap_s[s[r]])

            while (r-l+1) - maxf > k:
                hashmap_s[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

            

        


        
        