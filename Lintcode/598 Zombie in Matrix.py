from collections import deque
from pprint import pprint


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        if not grid or not grid[0]:
            return 0
        height = len(grid)
        width = len(grid[0])
        for h in range(height):
            for w in range(width):
                if grid[h][w] == 1:
                    queue = deque()
                    queue.append((h, w, 0))
                    while queue:
                        ch, cw, day = queue.popleft()
                        new_h = [ch + 1, ch - 1, ch, ch]
                        new_w = [cw, cw, cw + 1, cw - 1]
                        for nh, nw in zip(new_h, new_w):
                            if 0 <= nh < height and 0 <= nw < width and (grid[nh][nw] == 0 or grid[nh][nw] < day - 1):
                                grid[nh][nw] = day - 1
                                queue.append((nh, nw, day - 1))
        days = float("inf")
        for h in range(height):
            for w in range(width):
                if grid[h][w] == 0:
                    return -1
                days = min(days, grid[h][w])
        return -days
