# Based on largest_rectangle_in_histagram 84


def maximal_rectrangle_in_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    # Append extra 0 to the end, to mark the end of the curr row
    curr_row = [0] * (len(matrix[0]) + 1)
    ans = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == '1':
                curr_row[column] += 1
            else:
                curr_row[column] = 0
        stack = [-1]
        # print(curr_row)
        for curr_index, height in enumerate(curr_row):
            while height < curr_row[stack[-1]]:
                prev_index = stack.pop()
                h = curr_row[prev_index]
                w = curr_index - stack[-1] - 1
                ans = max(ans, h * w)
                # print(ans, curr_index, prev_index)
            stack.append(curr_index)
    return ans


# print(maximal_rectrangle_in_matrix([["0", "1"], ["1", "0"]]))
print(maximal_rectrangle_in_matrix([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))


def maximalRectangle_new(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0
    for row in matrix:
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack = [-1]
        # print(height)
        for i in range(n + 1):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
            stack.append(i)
    return ans


# print(maximal_rectrangle_in_matrix([["0", "1"], ["1", "0"]]))
print(maximalRectangle_new([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))
