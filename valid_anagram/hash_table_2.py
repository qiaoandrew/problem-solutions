def is_anagram(s, t):
    if len(s) != len(t):
        return False
    letters = {}
    for i in range(len(s)):
        if s[i] in letters:
            letters[s] += 1
        else:
            letters[s] = 1
        if t[i] in letters:
            letters[t] -= 1
        else:
            letters[t] = -1
    for value in letters.values():
        if value != 0:
            return False
    return True
