from collections import Counter


def character_replacement(s, k):
    max_frequency = 0
    left = 0
    occurences = Counter()
    for right in range(len(s)):
        occurences[s[right]] += 1
        max_frequency = max(max_frequency, occurences[s[right]])
        if right - left + 1 > max_frequency + k:
            occurences[s[left]] -= 1
            left += 1
    return len(s) - left


print(character_replacement('AABABBA', 1))