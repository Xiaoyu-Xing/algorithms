class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        i = 1
        total = 0
        while i * i <= num:
            if num % i == 0:
                total += i + num // i
            if i * i == num:
                total -= i
            i += 1
        return total - num == num
