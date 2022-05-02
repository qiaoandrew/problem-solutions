def length_of_longest_susbtring(s):
    left = 0
    indices = {}
    max_len = 0
    for right in range(len(s)):
        if s[right] in indices:
            left = max(left, indices[s[right]] + 1)
        max_len = max(max_len, right - left + 1)
        indices[s[right]] = right
    return max_len