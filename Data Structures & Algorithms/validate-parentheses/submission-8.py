class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        res = []

        # first elem cannot be a closing bracket
        if s[0] in [')', '}', ']'] or len(s) == 1:
            return False
        
        for i in range(0, len(s)):
            if s[i] in [')', '}', ']']:
                if not res:
                    return False
                val = res.pop()
                if val != parenthesis_map[s[i]]:
                    return False
            else:
                res.append(s[i])
            print(res)
        return len(res) == 0

                




            


        