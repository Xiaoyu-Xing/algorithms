# Returns the longest repeating non-overlapping
# substring in str


def longestRepeatedSubstring(str):
    n = len(str)
    mem = [[0 for x in range(n + 1)]
           for y in range(n + 1)]
    res = ""  # To store result
    res_length = 0  # To store length of result
    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # (j-i) > mem[i-1][j-1] to remove
            # overlapping
            if (str[i - 1] == str[j - 1] and
                    mem[i - 1][j - 1] < (j - i)):
                mem[i][j] = mem[i - 1][j - 1] + 1
                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if (mem[i][j] > res_length):
                    res_length = mem[i][j]
                    # It's the same storing i or j, 
                    # they point to the same sustring end index
                    index = i
            else:
                mem[i][j] = 0
    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if res_length > 0:
        # We only know the end index and length.
        for i in range(index - res_length + 1,
                       index + 1):
            res = res + str[i - 1]
    return res


print(longestRepeatedSubstring('geeksforgeeks'))
