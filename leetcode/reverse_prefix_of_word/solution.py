from collections import deque


def reverse_prefix(word, ch):
    if ch not in word:
        return word
    letters = deque()
    found_ch = False
    for i in range(len(word)):
        if found_ch:
            letters.append(word[i])
        else:
            letters.appendleft(word[i])
        if word[i] == ch:
            found_ch = True
    return ''.join(letters)
