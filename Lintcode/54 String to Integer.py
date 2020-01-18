class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def atoi(self, s):
        if not s:
            return 0
        s = s.strip()
        negative = False
        if s[0] == "-":
            negative = True
            s = s[1:]
        if s[0] == "+":
            s = s[1:]
        ans = 0
        for char in s:
            if not char.isdigit():
                break
            ans = ans * 10 + int(char)
            if negative and ans > 2147483648:
                return -2147483648
            elif not negative and ans > 2147483647:
                return 2147483647
        return ans if not negative else -ans
