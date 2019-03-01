class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) method, out loop is n, inner expand palindrome cost at most n for each checking
        if not s or len(s) < 2:
            return s
        result = ''
        for i in range(len(s)):
            even = self.expand_palindrome(s, i, i + 1)
            odd = self.expand_palindrome(s, i, i)
            result = max(even, odd, result, key=len)
        return result

    def expand_palindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        # Because i was overmoved one step left, j overmoved one step right
        # But slicing is exclusive on right.
        # print(i, j)
        return s[i + 1: j]
