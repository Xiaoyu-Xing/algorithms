# First method: by using slicing
# Time complexity of this solution is O(n * w^2) n being length of the list,
# w being the average word length. It is not better or worse than O(n^2),
# if the average word length is very long this solution is very slow,
# but with very long list and every word is very short this is a much better solution.


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def palindromePairs(words):
    solution = set()
    words_dict = {}
    for i, word in enumerate(words):
        words_dict[word] = i
    # print(words_dict)
    for word, i in words_dict.items():
        for j in range(len(word) + 1):
            prefix = word[:j]
            surfix = word[j:]
            back_pre = prefix[::-1]
            back_sur = surfix[::-1]
            if is_palindrome(prefix) and back_sur in words_dict:
                k = words_dict[back_sur]
                if i != k:
                    solution.add((k, i))
            if is_palindrome(surfix) and back_pre in words_dict:
                k = words_dict[back_pre]
                if i != k:
                    solution.add((i, k))
            # print(solution)
    return [list(i) for i in solution]


print(palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(palindromePairs(["bat", "tab", "cat"]))


# Trie version: use dictionary as trie node, and special key as termination of word
# Trie: https://www.youtube.com/watch?v=AXjmTQ8LEoI
# python trie: https://fizzbuzzed.com/top-interview-questions-5/
# Not correct yet.
class TrieNode:
    def __init__(self):
        self.next = {}
        self.end = -1
        self.next_palindrom = set()


class Solution:
    def palindromePairs(self, words):
        root = TrieNode()
        for i, word in enumerate(words):
            # print(word)
            trie = root
            for j in range(len(word) - 1, -1, -1):
                char = word[j]
                if char not in trie.next:
                    trie.next[char] = TrieNode()
                    if j > 0 and self.is_palindrome(word[:j]):
                        trie.next_palindrom.add(i)
                    if j != 0:
                        trie = trie.next[char]
            trie.end = i

        # print(root.next, root.end, root.next_palindrom, root.next['a'])
        solution = set()
        for i, word in enumerate(words):
            trie = root
            if word == '':
                for k, new_word in enumerate(words):
                    if i != k:
                        solution.add((i, k))
                        solution.add((k, i))
            for j in range(len(word)):
                if word[j] not in trie.next:
                    break
                if trie.end != -1 and trie.end != i and self.is_palindrome(word[j + 1:]):
                    solution.add((trie.end, i))
                if j == len(word) - 1 and trie.next_palindrom:
                    for each in trie.next_palindrom:
                        solution.add((i, each))
                trie = trie.next[word[j]]
            # print(word, solution)

        return [list(i) for i in solution]

    def is_palindrome(self, word):
        return word == word[::-1]


palindrome_pair_builder = Solution()
print(palindrome_pair_builder.palindromePairs(
    ["abcd", "dcba", "lls", "s", "sssll"]))
print(palindrome_pair_builder.palindromePairs(
    ["bat", "tab", "cat"]))
print(palindrome_pair_builder.palindromePairs(
    ['a', '']))


# Other's method:
class Trie:
    def __init__(self):
        # letter -> next trie node.
        self.paths = defaultdict(Trie)
        # If a word ends at this node, then this will be a positive value
        # that indicates the location of the word in the input list.
        self.wordEndIndex = -1
        # Stores all words that are palindromes from this node to end of word.
        # e.g. if we are on a path 'a','c' and word "babca" exists in this trie
        # (words are added in reverse), then "acbab"'s index will be in this
        # list since "bab" is a palindrome.
        self.palindromesBelow = []

    # Adds a word to the trie - the word will be added in
    # reverse (e.g. adding abcd adds the path d,c,b,a,$index) to the trie.
    # word - string the word to be added
    # index - int index of the word in the list, used as word identifier.
    def addWord(self, word, index):
        trie = self
        for j, char in enumerate(reversed(word)):
            if isPalindrome(word[0:len(word) - j]):
                trie.palindromesBelow.append(index)
            trie = trie.paths[char]
        trie.wordEndIndex = index


def makeTrie(words):
    trie = Trie()
    for i, word in enumerate(words):
        trie.addWord(word, i)
    return trie


# Takes the trie, a word, and its index in the word array
# and returns the index of every word that could be appended
# to it to form a palindrome.
def getPalindromesForWord(trie, word, index):
    # Walk trie. Every time we find a word ending,
    # we need to check if we could make a palindrome.
    # Once we get to the end of the word, we must check
    # all endings below for palindromes (they are already
    # stored in 'palindromesBelow').
    output = []
    while word:
        if trie.wordEndIndex >= 0:
            if isPalindrome(word):
                output.append(trie.wordEndIndex)
        if not word[0] in trie.paths:
            return output
        trie = trie.paths[word[0]]
        word = word[1:]

    if trie.wordEndIndex >= 0:
        output.append(trie.wordEndIndex)
    output.extend(trie.palindromesBelow)
    return output


def palindromePairs(words):
    trie = makeTrie(words)
    output = []
    for i, word in enumerate(words):
        candidates = getPalindromesForWord(trie, word, i)
        output.extend([[i, c] for c in candidates if i != c])
    return output
