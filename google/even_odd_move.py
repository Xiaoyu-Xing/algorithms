def solution(A):
    # write your code in Python 3.6
    length = len(A)
    next_high, next_low = [0] * length, [0] * length
    stack = []
    first = [(number, i) for i, number in enumerate(A)]
    first.sort(key=lambda x: x[0])
    print(first)
    for (number, i) in first:
        while stack and stack[-1] < i and A[stack[-1]] < number:
            next_high[stack.pop()] = i
        stack.append(i)
    stack = []
    second = [(-number, i) for i, number in enumerate(A)]
    # second = first[::-1]
    second.sort(key=lambda x: x[0])
    print(second)
    for number, i in second:
        while stack and stack[-1] < i and A[stack[-1]] > -number:
            next_low[stack.pop()] = i
        stack.append(i)
    high, low = [0] * length, [0] * length
    high[-1] = 1
    low[-1] = 1
    for i in range(length - 1)[::-1]:
        high[i] = low[next_high[i]]
        low[i] = high[next_low[i]]
    print(high, low)
    return sum()


print(solution([10, 13, 12, 14, 15]))
print(solution([10, 11, 14, 11, 10]))
