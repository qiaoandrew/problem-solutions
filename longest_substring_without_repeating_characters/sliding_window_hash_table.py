def length_of_longest_substring(s):
    max_length = 0
    hash_table = {}
    left = 0
    for right in range(len(s)):
        if s[right] in hash_table:
            left = max(hash_table[s[right]], left)
        max_length = max(max_length, right - left + 1)
        hash_table[s[right]] = right + 1
    return max_length
