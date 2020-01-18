class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """

    def romanToInt(self, s):
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        ans = 0
        while i < len(s):
            if i + 1 < len(s) and ROMAN[s[i]] < ROMAN[s[i + 1]]:
                ans += ROMAN[s[i + 1]] - ROMAN[s[i]]
                i += 2
            else:
                ans += ROMAN[s[i]]
                i += 1
        return ans

# https://www.jiuzhang.com/solution/roman-to-integer/#tag-highlight-lang-python