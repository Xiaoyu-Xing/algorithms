# time complexity could be O(n^3), three for loops
# and the same for space, list size n, each cell


def wordBreak(s, wordDict):
    results = [[] for _ in range(len(s) + 1)]
    results[len(s)] = ['']
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in wordDict:
                for prev in results[j]:
                    new_list = [s[i:j]]
                    # print(new_list)
                    new_list.extend(prev)
                    results[i].append(new_list)
    ret = []
    for each in results[0]:
        ret.append(' '.join(each))
    return ret


def wordBreak_2(s, wordDict):
    results = [[] for _ in range(len(s) + 1)]
    results[len(s)] = ['']
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in wordDict:
                for prev in results[j]:
                    if prev == '':
                        results[i].append(s[i:j])
                    else:
                        results[i].append(s[i:j] + ' ' + prev)
    return results[0]


# recurrisve method by forward backtracking and memorization
def wordBreak_recurrsive(s, wordDict):
    mem = {}
    return recurrsive_solution(s, wordDict, mem)


def recurrsive_solution(s, wordDict, mem):
    if s in mem:
        return mem[s]
    if not s:
        return ['']
    new_list = []
    for i in range(1, len(s) + 1):
        if s[:i] in wordDict:
            prev = recurrsive_solution(s[i:], wordDict, mem)
            for each in prev:
                print(each)
                if each == '':
                    new_list.append(s[:i])
                else:
                    new_list.append(s[:i] + ' ' + each)
    mem[s] = new_list
    print(mem)
    return new_list


print(wordBreak_recurrsive("catsanddog", [
      "cat", "cats", "and", "sand", "dog"]))
