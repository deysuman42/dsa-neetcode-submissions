class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        
        for j in t:
            if j in h:
                h[j] -= 1
            else:
                return False
        
        for i in h.keys():
            if h[i] !=0:
                return False
        return True
            


        