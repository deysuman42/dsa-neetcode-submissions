class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        

        def dfs(r, c):
            perim = 0
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            if grid[r][c] == 2:
                return 0
            grid[r][c] = 2

            for dr, dc in directions:
                perim += dfs(r + dr, c + dc)
            return perim
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)
            
        
        