class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # need hashmap
        need = {}
        for i in t:
            need[i] = need.get(i, 0) + 1
        required = len(need)

        window = {}
        formed = 0
        best_left = -1
        best_right = -1
        best_len = float('inf')
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right] , 0) + 1
            if (s[right] in need) and window[s[right]] == need[s[right]]:
                formed += 1
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left, best_right = left, right
            
                window[s[left]] -= 1
                if (s[left] in need) and window[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        return "" if best_left == float('inf') else s[best_left: best_right + 1]

            
        
        
       