class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9

# See https://www.lintcode.com/problem/add-digits/note/192463