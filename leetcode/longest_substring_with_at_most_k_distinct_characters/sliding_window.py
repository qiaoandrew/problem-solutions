def length_of_longest_substring_k_disinct(s, k):
    cur_chars = {}
    longest = 0
    left = 0
    for right in range(len(s)):
        cur_chars[s[right]] = cur_chars.get(s[right], 0) + 1
        while len(cur_chars) > k:
            cur_chars[s[left]] -= 1
            if cur_chars[s[left]] == 0:
                cur_chars.pop(s[left])
            left += 1
        longest = max(longest, right - left + 1)
    return longest