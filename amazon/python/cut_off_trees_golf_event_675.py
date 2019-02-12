# BFS, Map, overtime
class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        height = len(forest)
        if height == 0:
            return 0
        width = len(forest[0])
        if width == 0:
            return 0
        trees = []
        for i in range(height):
            for j in range(width):
                if forest[i][j] > 0:
                    trees.append((forest[i][j], i, j))
        trees.sort(key=lambda x: x[0])
        # print(trees)
        count = 0
        sr = 0
        sc = 0
        for (_, tr, tc) in trees:
            dist = self.dist(forest, sr, sc, tr, tc)
            if dist < 0:
                return -1
            count += dist
            sr, sc = tr, tc
        return count

    def dist(self, forest, sr, sc, tr, tc):
        # print(sr, sc, tr, tc)
        height = len(forest)
        width = len(forest[0])
        queue = collections.deque()
        queue.append((sr, sc, 0))
        seen = [[False for i in range(width)] for j in range(height)]
        seen[sr][sc] = True
        # print(seen)
        # print(queue)
        while queue:
            (nowr, nowc, nowdist) = queue.popleft()
            # print(nowr, nowc, nowdist)
            if nowr == tr and nowc == tc:
                return nowdist
            for nr, nc in ((nowr - 1, nowc), (nowr + 1, nowc), (nowr, nowc - 1), (nowr, nowc + 1)):
                if (0 <= nr < height and 0 <= nc < width and seen[nr][nc] == False and forest[nr][nc]):
                    seen[nowr][nowc] = True
                    queue.append((nr, nc, nowdist + 1))
            # print(queue)
        return -1

# My method, 8s


class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        height = len(forest)
        if height == 0:
            return 0
        width = len(forest[0])
        if width == 0:
            return 0
        trees = []
        for i in range(height):
            for j in range(width):
                if forest[i][j] > 0:
                    trees.append((forest[i][j], i, j))
        trees.sort(key=lambda x: x[0])
        # print(trees)
        count = 0
        sr = 0
        sc = 0
        for (_, tr, tc) in trees:
            dist = self.dist(forest, sr, sc, tr, tc)
            if dist < 0:
                return -1
            count += dist
            sr, sc = tr, tc
        return count

    def dist(self, forest, sr, sc, tr, tc):
        # print(sr, sc, tr, tc)
        height = len(forest)
        width = len(forest[0])
        queue = collections.deque()
        queue.append((sr, sc, 0))
        seen = [[False for i in range(width)] for j in range(height)]
        # seen[sr][sc] = True
        # print(seen)
        # print(queue)
        while len(queue) != 0:
            (nowr, nowc, nowdist) = queue.popleft()
            # print(nowr, nowc, nowdist)
            if nowr < 0 or nowr >= height or nowc < 0 or nowc >= width or seen[nowr][nowc] or forest[nowr][nowc] <= 0:
                continue
            if nowr == tr and nowc == tc:
                return nowdist
            seen[nowr][nowc] = True
            queue.extend([(nowr + i, nowc + j, nowdist + 1)
                          for i, j in zip([1, -1, 0, 0], [0, 0, 1, -1])])
            # print(queue)
        return -1
