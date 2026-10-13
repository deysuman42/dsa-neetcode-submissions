class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(t[i]) - ord('a')] -= 1

        for i in s_count:
            if i != 0:
                return False
        return True

        
            
        