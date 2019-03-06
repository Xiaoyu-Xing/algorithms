from collections import defaultdict, deque


# with BFS, adjacent list, and indgree list (actually dictionary of sets)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        children = defaultdict(set)
        parents = defaultdict(set)
        for pair in prerequisites:
            parents[pair[0]].add(pair[1])
            children[pair[1]].add(pair[0])
        queue = deque()
        for i in range(numCourses):
            if i not in parents:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            for child in children[curr]:
                parents[child].remove(curr)
                if len(parents[child]) == 0:
                    queue.append(child)
        for _, parent in parents.items():
            if len(parent) != 0:
                return False
        return True