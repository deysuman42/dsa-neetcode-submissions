class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        n = len(tokens)
        for i in range(0, n):
            if tokens[i] == '+':
                val = res[-2] + res[-1]
                res.pop()
                res.pop()
                res.append(val)
            elif tokens[i] == '*':
                val = res[-2] * res[-1]
                res.pop()
                res.pop()
                res.append(val)
            elif tokens[i] == '-':
                val = res[-2] - res[-1]
                res.pop()
                res.pop()
                res.append(val)
            elif tokens[i] == '/':
                val = int(res[-2] / res[-1])
                res.pop()
                res.pop()
                res.append(val)
            else:
                res.append(int(tokens[i]))
          
        return res[-1]
        