class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev = 0
        for each in logs:
            func, start_end, time = each.split(':')
            func, time = int(func), int(time)
            if start_end == 'start':
                if stack:
                    ans[stack[-1]] += time - prev
                stack.append(func)
                prev = time
            else:
                ans[stack.pop()] += time - prev + 1
                prev = time + 1
        return ans
