import re


def longest_substring_without_repeating_characters(s):
    left = 0
    count = {}
    max_length = 0

    for right in range(len(s)):
        while s[right] in count:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                count.pop(s[left])
            left += 1

        count[s[right]] = count.get(s[right], 0) + 1
        max_length = max(max_length, right - left + 1)

    return max_length