from collections import defaultdict


def group_anagrams(strs):
    anagram_map = defaultdict(list)
    for string in strs:
        anagram_id = "".join(sorted(string))
        anagram_map[anagram_id].append(string)
    return list(anagram_map.values())