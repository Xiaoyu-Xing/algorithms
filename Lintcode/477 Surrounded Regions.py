from collections import deque


class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def surroundedRegions(self, board):
        if not board or not board[0]:
            return board
        height = len(board)
        width = len(board[0])
        self.conn = {}

        for i in range(height):
            self.bfs(board, i, 0)
            self.bfs(board, i, width - 1)

        for j in range(width):
            self.bfs(board, 0, j)
            self.bfs(board, height - 1, j)

        for i in range(height):
            for j in range(width):
                if board[i][j] == "Visited":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board

    def bfs(self, board, x, y):
        height = len(board)
        width = len(board[0])
        if board[x][y] != "O":
            return
        queue = deque()
        queue.append((x, y))
        board[x][y] = "Visited"
        while queue:
            cx, cy = queue.popleft()
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            for nx, ny in zip(dx, dy):
                nx += cx
                ny += cy
                if 0 <= nx < height and 0 <= ny < width and board[nx][ny] == "O":
                    board[nx][ny] = "Visited"
                    queue.append((nx, ny))
