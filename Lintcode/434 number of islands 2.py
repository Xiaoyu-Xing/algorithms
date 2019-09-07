"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    def __init__(self):
        self.connectivity = {}
        self.count = 0

    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        if not operators:
            return []
        result = []
        for ope in operators:
            curr_x = ope.x
            curr_y = ope.y
            curr_point = (curr_x, curr_y)
            if curr_point not in self.connectivity:
                self.connectivity[curr_point] = curr_point
                self.count += 1
            new_xs = [curr_x, curr_x, curr_x + 1, curr_x - 1]
            new_ys = [curr_y + 1, curr_y - 1, curr_y, curr_y]
            for new_point in zip(new_xs, new_ys):
                if new_point in self.connectivity and self.union(new_point, curr_point):
                    self.count -= 1
            result.append(self.count)
        return result

    def find_root(self, node):
        if self.connectivity[node] != node:
            self.connectivity[node] = self.find_root(self.connectivity[node])
        return self.connectivity[node]

    def union(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 != root2:
            self.connectivity[root1] = root2
            return True
        return False
