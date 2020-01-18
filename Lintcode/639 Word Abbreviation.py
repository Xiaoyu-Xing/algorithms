from collections import defaultdict


class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """

    def wordsAbbreviation(self, dictionary):
        if not dictionary:
            return []
        abbr = defaultdict(int)
        # When need to maintain order, it's quite easy to just build the array and loop through by index,
        # rather than use some of the complex data structure, like OrderedDict
        ans = [None for _ in range(len(dictionary))]
        for i, word in enumerate(dictionary):
            curr_abbr = self.rule(word)
            abbr[curr_abbr] += 1
            ans[i] = curr_abbr

        round = 1
        while True:
            is_unique = True
            round += 1
            # It's easier to loop by index, rather than loop the dictionary
            for i in range(len(dictionary)):
                if abbr[ans[i]] > 1:
                    is_unique = False
                    curr_abbr = self.rule(dictionary[i], round)
                    abbr[curr_abbr] += 1
                    ans[i] = curr_abbr
            if is_unique:
                break
        return ans

    def rule(self, word, prefix_count=1):
        if len(word) <= 2 + prefix_count:
            return word
        return word[0:prefix_count] + str(len(word) - 1 - prefix_count) + word[-1]
