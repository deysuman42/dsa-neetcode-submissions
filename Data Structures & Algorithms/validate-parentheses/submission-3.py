class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        key_values = {')':'(',
        '}':'{', ']':'['
        }

        for i in s:
            if i == '(' or i == '{' or i == '[':
                l.append(i)
            else:
                if l:
                    if l[-1] == key_values[i]:
                        l.pop()
                    else:
                        return False

                else:
                    return False
        return l == []