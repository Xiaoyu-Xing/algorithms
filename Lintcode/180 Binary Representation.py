class Solution:
    """
    @param n: Given a decimal number that is passed in as a string
    @return: A string
    """

    def binaryRepresentation(self, n):
        if "." in n:
            n_str = str(n).split(".")
            integer = int(n_str[0])
            decimal = float("0." + n_str[1])
        else:
            integer = int(n)
            decimal = 0
        ans = collections.deque()
        while integer > 0:
            ans.appendleft(str(integer % 2))
            integer = integer // 2
        ans_decimal = []
        while decimal > 0:
            decimal *= 2
            if decimal >= 1:
                ans_decimal.append("1")
                decimal -= 1
            else:
                ans_decimal.append("0")
            if len(ans_decimal) > 32:
                return "ERROR"
        if not ans:
            ans.append("0")
        return "".join(ans) + "." + "".join(ans_decimal) if ans_decimal else "".join(ans)


# https://www.jiuzhang.com/solution/binary-representation/#tag-highlight-lang-python