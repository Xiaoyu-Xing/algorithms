# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """


class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def match(word1, word2):
            return sum([w1 == w2 for w1, w2 in zip(word1, word2)])

        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(
                wordlist, 2) if match(w1, w2) == 0)
            guess = min(wordlist, key=lambda w: count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if match(w, guess) == n]

# OR:


class Solution:
    def match(self, word1, word2):
        return sum([w1 == w2 for w1, w2 in zip(word1, word2)])

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0
        while n < 6:
            guess = random.choice(wordlist)
            n = master.guess(guess)
            if n == 6:
                return
            wordlist = [word for word in wordlist if self.match(
                word, guess) == n and word != guess]
