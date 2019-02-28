# DFS
def num_of_islands(grid):
    if not grid:
        return 0
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if int(grid[i][j]) == 1:
                mark_by_dfs(grid, i, j)
                result += 1
    return result


# this function is just to mark all connected 1s to 0s by DFS
# in four directions, right, left, down, up, repectively
def mark_by_dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or\
            int(grid[i][j]) != 1:
        return
    grid[i][j] = 0
    mark_by_dfs(grid, i, j + 1)
    mark_by_dfs(grid, i, j - 1)
    mark_by_dfs(grid, i + 1, j)
    mark_by_dfs(grid, i - 1, j)

# DFS time O(m*n) space 0o(m*n)


# BFS
def num_of_islands(grid):
    if not grid:
        return 0
    result = 0
    queue = collections.deque()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if int(grid[i][j]) == 1:
                queue.append((i, j))
                mark_by_bfs(queue, grid, i, j)
                result += 1
    return result


def mark_by_bfs(queue, grid, i, j):
    while queue:
        i, j = queue.popleft()
        if 0 <= i < len(grid) and\
                0 <= j < len(grid[i]) and\
                grid[i][j] == '1':
            grid[i][j] = 0
            queue.extend([(i, j + 1), (i, j - 1),
                          (i + 1, j), (i - 1, j)])

# Aggregate together the helper function
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        queue = [] # implement as deque will be BFS, as [] will be DFS
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    queue.append((i, j))
                    while queue:
                        ci, cj = queue.pop()
                        if 0 <= ci < height and 0 <= cj < width and grid[ci][cj] == '1':
                            grid[ci][cj] = '0'
                            queue.append((ci + 1, cj))
                            queue.append((ci - 1, cj))
                            queue.append((ci, cj + 1))
                            queue.append((ci, cj - 1))
                    counter += 1
        return counter