def length_of_longest_substring(s):
    if len(s) == 0: return 0
    left = 0
    longest = 1
    for right in range(1, len(s)):
        if s[right] not in s[left:right]:
            longest = max(longest, right - left + 1)
        else:
            left += 1
            while left < right and (s[right] in s[left:right]):
                left += 1
    return longest


print(length_of_longest_substring("nfpdmpi"))
