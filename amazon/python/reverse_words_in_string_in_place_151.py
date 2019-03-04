class Solution:
    def reverseWords(self, s):
        s = list(s)
        self.shift_trim(s)
        self.reverse(s, 0, len(s) - 1)
        # print(s)
        start = 0
        for end in range(len(s)):
            if end == len(s) - 1:
                self.reverse(s, start, end)
            if s[end] == ' ':
                self.reverse(s, start, end - 1)
                start = end + 1
        return ''.join(s)

    def reverse(self, x, i, j):
        while i < j:
            x[i],  x[j] = x[j], x[i]
            i += 1
            j -= 1

    def shift_trim(self, x):
        i = 0
        for j in range(len(x)):
            if i > 0 and x[i - 1] != ' ' or x[j] != ' ':
                x[i] = x[j]
                if j > i:
                    x[j] = ' '
                i += 1
        while x and x[-1] == ' ':
            del x[-1]


solver = Solution()
print(solver.reverseWords("the sky is blue"))
print(solver.reverseWords("  s  "))


# Another way:
class Solution:
    def reverseWords(self, s):
        s = list(s)
        self.shift_trim(s)
        self.reverse(s, 0, len(s) - 1)
        start = 0
        s.append(' ')
        for end in range(len(s)):
            if s[end] == ' ':
                self.reverse(s, start, end - 1)
                start = end + 1
        del s[-1]
        return ''.join(s)

    def reverse(self, x, i, j):
        while i < j:
            x[i],  x[j] = x[j], x[i]
            i += 1
            j -= 1

    def shift_trim(self, x):
        i = 0
        for j in range(len(x)):
            # Meeting ' '
            if x[j] == ' ':
                # Don't add space in beginning, nor duplicate spaces
                if i > 0 and x[i - 1] != ' ':
                    # add a space and move i forward
                    x[i] = ' '
                    i += 1
            # Now meeting chars
            else:
                # Write j to i place
                x[i] = x[j]
                # Overwrite current
                if i != j:
                    x[j] = ' '
                i += 1
        while x and x[-1] == ' ':
            x.pop()
