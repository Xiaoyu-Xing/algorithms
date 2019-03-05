# Reference:
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems


# Sliding window + hash
def find_anagrams(s, p):
    res = []
    if len(s) < len(p):
        return []
    s_dict = {}
    p_dict = {}
    for letter in p:
        p_dict[letter] = p_dict.get(letter, 0) + 1
    for letter in s[:len(p) - 1]:
        s_dict[letter] = s_dict.get(letter, 0) + 1
    for i in range(len(p) - 1, len(s)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        if i - len(p) >= 0:
            s_dict[s[i - len(p)]] -= 1
            if s_dict[s[i - len(p)]] == 0:
                del s_dict[s[i - len(p)]]
        if s_dict == p_dict:
            res.append(i - len(p) + 1)
    return res
