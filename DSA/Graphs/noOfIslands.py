from typing import List
class Solution:
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] in ("0", "#"):
            return
        grid[i][j] = "#"
        for v, h in Solution.directions:
            self.dfs(grid, i + v, j + h)
    def numIslands(self, grid:List[List[int]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j)
        return islands