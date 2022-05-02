def character_replacement(s, k):
    left, max_length, max_repeat_letter_count = 0, 0, 0
    frequencies = {}
    for right in range(len(s)):
        frequencies[s[right]] = frequencies.get(s[right], 0) + 1
        max_repeat_letter_count = max(max_repeat_letter_count,
                                      frequencies[s[right]])
        if right - left + 1 > k + max_repeat_letter_count:
            frequencies[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length
