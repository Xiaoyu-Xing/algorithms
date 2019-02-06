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
# Find exactly k distinct letters


def countkDist(str1, k):
    n = len(str1)

    # Initialize result
    res = 0

    # To store count of characters from
    # 'a' to 'z'
    cnt = [0] * 27

    # Consider all substrings beginning
    # with str[i]
    for i in range(0, n):
        dist_count = 0

        # Initializing array with 0
        cnt = [0] * 27

        # Consider all substrings between str[i..j]
        for j in range(i, n):

            # If this is a new character for this
            # substring, increment dist_count.
            if(cnt[ord(str1[j]) - 97] == 0):
                dist_count += 1

            # Increment count of current character
            cnt[ord(str1[j]) - 97] += 1

            # If distinct character count becomes k,
            # then increment result.
            if(dist_count == k):
                res += 1
            if(dist_count > k):
                break

    return res
