def count_good_substring(s):
    if len(s) < 3:
        return 0
    left = 0
    good_substrings = 0
    letters = {}
    for right in range(len(s)):
        letters[s[right]] = letters.get(s[right], 0) + 1
        while letters[s[right]] > 1:
            letters[s[left]] -= 1
            left += 1
        if right - left + 1 == 3:
            good_substrings += 1
            letters[s[left]] -= 1
            left += 1
    return good_substrings
