class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # very important to check the new repeating char is after left, otherwise left will move back
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcde'))
    print(solution.lengthOfLongestSubstring('cabcdea'))
