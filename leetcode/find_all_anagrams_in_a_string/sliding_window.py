def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    p_letters, s_letters = {}, {}
    start_indices = []
    for i in range(len(s)):
        s_letters[s[i]] += 1
        if i >= len(p):
            s_letters[s[i - len(p)]] -= 1
            if s_letters[s[i - len(p)]] == 0:
                s_letters.pop(s[i - len(p)])
        if p_letters == s_letters:
            start_indices.append(i - len(p) + 1)
    return start_indices