def length_of_longest_substring(s):
    left, right = 0, 0
    letters = [0] * 128
    longest = 0
    while right < len(s):
        right_letter = s[right]
        letters[ord(right_letter)] += 1
        while letters[ord(right_letter)] > 1:
            left_letter = s[left]
            letters[ord(left_letter)] -= 1
            left += 1
        longest = max(longest, right - left + 1)
        right += 1
    return longest


print(length_of_longest_substring('bbbbb'))