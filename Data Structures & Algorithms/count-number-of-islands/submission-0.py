from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def markLand(i: int, j: int):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            if grid[i][j] != "1":
                return

            grid[i][j] = "0"

            markLand(i + 1, j)
            markLand(i - 1, j)
            markLand(i, j + 1)
            markLand(i, j - 1)

        counter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    counter += 1
                    markLand(i, j)

        return counter