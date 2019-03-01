class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if 1 <= ord(i) - ord(stack[-1]) <= 2:
                    stack.pop()
                else:
                    stack.append(i)
        return not stack
