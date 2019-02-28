def lengthOfLongestSubstring(s: str) -> int:
    left = ans = 0
    dic = {}
    if not s or len(s) <= 1:
        return len(s)
    for i, letter in enumerate(s):
        if letter in dic and dic[letter] >= left:
            # very important to check the new repeating char is after left, otherwise left will move back
            left = dic[letter] + 1
            # Only necessary to update ans when no repeating,
            # because repeating shows up will definitely shorter than current ans
        else:
            ans = max(ans, i - left + 1)
        dic[letter] = i
        # print(dic, ans, left)
    return ans


print(lengthOfLongestSubstring("tmmzuxt"))
