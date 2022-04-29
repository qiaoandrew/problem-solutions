def length_of_longest_substring(s):
    if len(s) == 0:
        return 0
    left = 0
    longest = 0
    indices = {}
    for right in range(len(s)):
        if s[right] in indices:
            left = max(left, indices[s[right]] + 1)
        longest = max(longest, right - left + 1)
        indices[s[right]] = right
    return longest
