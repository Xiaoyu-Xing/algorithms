def lengthOfLongestSubstringKDistinct(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if not s or k == 0:
        return 0
    dic = collections.defaultdict(int)
    result = 0
    left = 0
    for i, letter in enumerate(s):
        dic[letter] += 1
        while len(dic) > k:
            dic[s[left]] -= 1
            if dic[s[left]] == 0:
                del dic[s[left]]
            left += 1
        result = max(result, i - left + 1)
    return result


# Or slightly better way:
def lengthOfLongestSubstringKDistinct(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if not s or k == 0:
        return 0
    dic = {}
    left = 0
    result = 0
    for i, letter in enumerate(s):
        dic[letter] = i
        if len(dic) > k:
            to_del = min(dic.values())
            del dic[s[to_del]]
            left = to_del + 1
        result = max(result, i - left + 1)
    return result
