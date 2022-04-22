def is_anagram(s, t):
    if len(s) != len(t):
        return False
    letters_s = {}
    for letter in s:
        if letter in letters_s:
            letters_s[letter] += 1
        else:
            letters_s[letter] = 1
    for letter in t:
        if letter in letters_s:
            if letters_s[letter] == 0:
                return False
            letters_s[letter] -= 1
        else:
            return False
    return True