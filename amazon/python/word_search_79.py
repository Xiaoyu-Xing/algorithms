def search_word(board, word):
    if not board or len(board) == 0:
        return False
    if not word:
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if search_DFS(board, i, j, word):
                return True
    return False


def search_DFS(board, i, j, word):
    if len(word) == 0:
        return True
    ans = False
    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
        temp = board[i][j]
        board[i][j] = ' '
        # print(temp)
        ans = search_DFS(board, i + 1, j, word[1:]) or \
            search_DFS(board, i - 1, j, word[1:]) or \
            search_DFS(board, i, j + 1, word[1:]) or \
            search_DFS(board, i, j - 1, word[1:])
        board[i][j] = temp
    return ans


# Inspired by this: https://leetcode.com/problems/word-search/discuss/27820/Python-DFS-solution
# The iterative solution need to bring same amount of "information" as the recurrsive solution
# for this question: these are the board, i, j, word(slicing or position to look for next), visited list(or mark it on the graph)

# Failed!!!! Cannot figure out how to differetiate the visited node for different trial.
# Need to prevent reuse past node like [['a', 'a']] for 'aaa'
# also need to prevent blocking different trial due to visited from last trial.
def search_word_iterative(board, word):
    if not board or len(board) == 0:
        return False
    if not word:
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if search_DFS_iterative(board, i, j, word):
                return True
    return False


def search_DFS_iterative(board, i, j, word):
    visited = {}
    stack = []
    # the stack need to know the below information:
    # coordinators and the position of word to look for.
    stack.append((i, j, 0))
    while stack:
        newi, newj, pos = stack.pop()
        try_counter = 0
        if pos == len(word):
            return True
        if (newi, newj) not in visited and \
                0 <= newi < len(board) and \
                0 <= newj < len(board[0]) and \
                board[newi][newj] == word[pos]:
            visited[newi, newj] = True
            print(visited)
            stack.append((newi + 1, newj, pos + 1))
            stack.append((newi - 1, newj, pos + 1))
            stack.append((newi, newj + 1, pos + 1))
            stack.append((newi, newj - 1, pos + 1))
    return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
board2 = [['a', 'a']]
board3 = [["A", "B", "C", "E"],
          ["S", "F", "E", "S"],
          ["A", "D", "E", "E"]]
word5 = "ABCESEEEFS"
word1 = 'ABCCED'
word2 = 'SEE'
word3 = 'ABCB'
word4 = 'aaa'
print(search_word(board3, word5))
print(search_word_iterative(board3, word5))
