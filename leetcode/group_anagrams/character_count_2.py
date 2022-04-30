from collections import defaultdict


def group_anagrams(strs):
    ans = defaultdict(list)
    for string in strs:
        count = [0] * 26
        for letter in string:
            count[ord(letter) - ord('a')] += 1
        ans[tuple(count)].append(string)
    return ans.values()
