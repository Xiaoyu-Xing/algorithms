# Using max heap to exclude those element beyong kth smaller ones
import heapq


def kClosest(points, k):
    def distance(point):
        return point[0] * point[0] + point[1] * point[1]

    counter = 0  # break ties in heapq
    pq = []
    for point in points:
        if len(pq) < k:
            heapq.heappush(pq, (-distance(point), counter, point))
        else:
            heapq.heappushpop(pq, (-distance(point), counter, point))
        counter += 1

    return [i for i in map(lambda x: x[2], pq)]


# Or by nsmallest element
class Solution(object):
    def kClosest(self, points, k):
        return heapq.nsmallest(k,
                               points,
                               key=lambda point: point[0] ** 2 + point[1] ** 2)


# Or by quickselect:
# Reference: https://leetcode.com/problems/k-closest-points-to-origin/discuss/220235/Java-Three-solutions-to-this-classical-K-th-problem.
# reference: https://en.wikipedia.org/wiki/Quickselect
# https://stackoverflow.com/questions/8783408/why-is-the-runtime-of-the-selection-algorithm-on


def quickSelect(points, low, high):
    def dist(i):
        return i[0] ** 2 + i[1] ** 2
    pivot = points[low]
    while low < high:
        while low < high and dist(points[high]) >= dist(pivot):
            high -= 1
        points[low] = points[high]
        while low < high and dist(points[low]) <= dist(pivot):
            low += 1
        points[high] = points[low]
    points[low] = pivot
    return low


def kClosest_n(points, k):
    high = length = len(points) - 1
    low = 0
    # Either use <= here, then use mid or k for return statement
    # or use < here, but use k for return statement
    while low <= high:
        mid = quickSelect(points, low, high)
        # print(low, high, mid)
        # print(points)
        if mid < k:
            low = mid + 1
        elif mid > k:
            high = mid - 1
        else:
            break
    return points[:mid]


points = [[3, 3], [5, -1], [-2, 4]]
points2 = [[-2, 10], [-4, -8], [10, 7], [-4, -7]]
K = 2
K2 = 3
print(kClosest_n(points2, K2))
