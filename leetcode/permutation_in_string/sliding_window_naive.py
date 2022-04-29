from collections import defaultdict


def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_letters, s2_letters = defaultdict(int), defaultdict(int)
    for i in range(len(s1)):
        s1_letters[s1[i]] += 1
        s2_letters[s2[i]] += 1
    left, right = 0, len(s1) - 1
    while True:
        if s1_letters == s2_letters:
            return True
        else:
            if s2_letters[s2[left]] == 1:
                s2_letters.pop(s2[left])
            else:
                s2_letters[s2[left]] -= 1
            left += 1
            right += 1
            if right < len(s2):
                s2_letters[s2[right]] += 1
            else:
                return False


print(check_inclusion('adc', 'dcda'))