from collections import deque


class Solution_With_Duplicate:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return rooms
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    self.bfs(rooms, row, col)
        return rooms

    def bfs(self, rooms, row, col):
        height = len(rooms)
        width = len(rooms[0])
        queue = deque()
        queue.append((row, col, 0))
        while queue:
            curr_row, curr_col, dis = queue.popleft()
            new_row = [curr_row + 1, curr_row - 1, curr_row, curr_row]
            new_col = [curr_col, curr_col, curr_col + 1, curr_col - 1]
            for nr, nc in zip(new_row, new_col):
                if 0 <= nr < height and 0 <= nc < width and rooms[nr][nc] > dis + 1:
                    rooms[nr][nc] = dis + 1
                    queue.append((nr, nc, dis + 1))


class Solution_Multiple_Source:  # Above solution has duplicate, rather use mutiple source to make sure one time visit
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return rooms
        queue = deque()
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        while queue:
            cx, cy = queue.popleft()
            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]
            for nx, ny in zip(dx, dy):
                nx += cx
                ny += cy
                if 0 <= nx < len(rooms) and 0 <= ny < len(rooms[0]) and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = rooms[cx][cy] + 1
                    queue.append((nx, ny))
        return rooms
