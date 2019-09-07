'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''

from operator import attrgetter


class Solution:
    def __init__(self):
        self.check_table = {}
        self.connectivity = []

    def organize_city(self, connections):
        count = 0
        check_table = {}
        for conn in connections:
            if conn.city1 not in check_table:
                check_table[conn.city1] = count
                count += 1
            if conn.city2 not in check_table:
                check_table[conn.city2] = count
                count += 1
        return check_table

    def find_root(self, connectivity, node):
        while connectivity[node] != node:
            node = connectivity[node]
        return node

    def union(self, connectivity, first_node, second_node):
        connectivity[first_node] = second_node

    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        if not connections:
            return []
        connections.sort(key=attrgetter("cost", "city1", "city2"))

        self.check_table = self.organize_city(connections)
        self.connectivity = [i for i in range(len(self.check_table))]

        result = []
        for conn in connections:
            first_root = self.find_root(self.connectivity, self.check_table[conn.city1])
            second_root = self.find_root(self.connectivity, self.check_table[conn.city2])
            if first_root != second_root:
                result.append(conn)
                self.union(self.connectivity, first_root, second_root)
        # print(result)
        if len(result) != len(self.check_table) - 1:
            return []
        return result
