# DP, recurrsive and memorization
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mem = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            mem[0][i] = 1
        for j in range(m):
            mem[j][0] = 1

        def find(m, n, mem):
            if mem[m][n]:
                return mem[m][n]
            mem[m][n] = find(m - 1, n, mem) + find(m, n - 1, mem)
            return mem[m][n]
        find(m - 1, n - 1, mem)
        return mem[m - 1][n - 1]


# or shorter code:
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mem = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                mem[i][j] = mem[i - 1][j] + mem[i][j - 1]
        return mem[m - 1][n - 1]
