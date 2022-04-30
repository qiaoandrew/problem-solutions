def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}
    for letter_s, letter_t in zip(s, t):
        if (letter_s not in map_s_to_t) and (letter_t not in map_t_to_s):
            map_s_to_t[letter_s] = letter_t
            map_t_to_s[letter_t] = letter_s
        elif map_s_to_t.get(letter_s) != letter_t or map_t_to_s.get(
                letter_t) != letter_s:
            return False
    return True


print(is_isomorphic('foo', 'bar'))