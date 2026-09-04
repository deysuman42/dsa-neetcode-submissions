class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        minop = float('inf')
        n = len(blocks)
        c = 0

        for r in range(n):
            if blocks[r] == 'W':
                c += 1
            if (r - left) + 1 == k:
                minop = min(minop, c)
                if blocks[left] == 'W':
                    c -= 1
                left += 1
        return minop
                


        