class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """

    def isStrobogrammatic(self, num):
        if not num:
            return True
        left, right = 0, len(num) - 1
        sym = {"1": "1", "6": "9", "8": "8", "9": "6", "0": "0"}
        single_sym = set(["0", "1", "8"])
        while left <= right:
            if num[right] not in sym or num[left] != sym[num[right]]:
                return False
            left += 1
            right -= 1
        return True
