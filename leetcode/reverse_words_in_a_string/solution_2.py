from collections import deque


def reverse_words(s):
    left, right = 0, len(s) - 1
    while left <= right and s[left] == ' ':
        left += 1
    while left <= right and s[right] == ' ':
        right -= 1

    words, cur_word = deque(), []
    while left <= right:
        if s[left] == ' ' and cur_word:
            words.appendleft(''.join(cur_word))
            cur_word = []
        elif s[left] != ' ':
            cur_word.append(s[left])
        left += 1
    words.appendleft(''.join(cur_word))

    return ' '.join(words)
