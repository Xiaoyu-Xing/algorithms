class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        ans = 1
        prev = 0
        for i in range(1, length):
            # it's necessary to check this equal, to prevent [1, 1, 1]
            if A[i - 1] == A[i]:
                prev = i
            if i == (length - 1) or not (A[i - 1] > A[i] < A[i + 1]) and not (A[i - 1] < A[i] > A[i + 1]):
                ans = max(ans, i - prev + 1)
                prev = i
        return ans


A = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(maxTurbulenceSize(A))


# or
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        ans = 1
        prev = 0
        for i in range(1, length):
            if A[i - 1] == A[i]:
                prev = i
            elif i == (length - 1) or (A[i - 1] - A[i]) * (A[i] - A[i + 1]) >= 0:
                ans = max(ans, i - prev + 1)
                prev = i
        return ans


# Or
def maxTurbulenceSize(self, A):
    best = clen = 0

    for i in range(len(A)):
        if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
            clen += 1
        elif i >= 1 and A[i - 1] != A[i]:
            clen = 2
        else:
            clen = 1
        best = max(best, clen)
    return best
