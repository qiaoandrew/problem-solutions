from collections import defaultdict


def group_strings(strings):

    def shift_letter(c, shift):
        return chr(((ord(c) - shift) % 26) + 97)

    def get_key(s):
        shift = ord(s[0]) - ord('a')
        return ''.join(shift_letter(c, shift) for c in s)

    groups = defaultdict(list)
    for s in strings:
        key = get_key(s)
        groups[key].append(s)
    return list(groups.values())
