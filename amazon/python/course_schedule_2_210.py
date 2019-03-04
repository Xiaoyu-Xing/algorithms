from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []
        children = defaultdict(set)
        parents = defaultdict(set)
        # Build dependency
        for req in prerequisites:
            children[req[1]].add(req[0])
            parents[req[0]].add(req[1])
        # Populate children dict in case some courses doesn't have child nor parents
        for i in range(numCourses):
            children[i]
        queue = deque()
        for course in children.keys():
            if course not in parents:
                queue.append(course)
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for child in children[curr]:
                parents[child].remove(curr)
                if len(parents[child]) == 0:
                    queue.append(child)

        for _, parent in parents.items():
            if len(parent) != 0:
                return []

        return ans


# Copied from:https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments.

# BFS
def findOrder1(self, numCourses, prerequisites):
    dic = {i: set() for i in xrange(numCourses)}
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    # queue stores the courses which have no prerequisites
    queue = collections.deque([i for i in dic if not dic[i]])
    count, res = 0, []
    while queue:
        node = queue.popleft()
        res.append(node)
        count += 1
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                queue.append(i)
    return res if count == numCourses else []

# DFS


def findOrder(self, numCourses, prerequisites):
    dic = collections.defaultdict(set)
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    stack = [i for i in xrange(numCourses) if not dic[i]]
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)
        dic.pop(node)
    return res if not dic else []
