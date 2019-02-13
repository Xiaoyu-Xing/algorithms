# 两个题基本都是基于Leetcode843题的。第一题是给你两个input words。让你计算两个input有多少个字母是一样的，不考虑顺序。Input是长度固定为五的不同字母组成的英文单词，这个function也需要有判断Input是不是valid的功能。输出是两个单词的相同字母数，输出为一个int。
# 第二个是输入是一个dictionary，dictionary里面是不同word和keyword放入第一问函数中的输出结果。还有另一个input是一个word。输出是这个input word有没有可能是keyword。
# 很像leetcode843题，楼主之前恰好刷过。当时对答如流，但是最后还是挂了。


def get_letter_num(word1, word2):
    if not is_valid(word1) or not is_valid(word2):
        return -1
    word1 = set(word1)
    word2 = set(word2)
    return len(word1.intersection(word2))


def is_valid(word):
    if len(word) > 5 or word not in English_word or len(set(word)) != 5:
        return False


English_word = {}
