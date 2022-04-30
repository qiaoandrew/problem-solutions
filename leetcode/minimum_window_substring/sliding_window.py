def min_window(s, t):
    if t == '' or len(t) > len(s):
        return ''

    count_s, count_t = {}, {}
    for letter in t:
        count_t[letter] = count_t.get(letter, 0) + 1

    have, need = 0, len(count_t)
    res, res_len = [-1, -1], float('infinity')
    left = 0
    for right in range(len(s)):
        letter = s[right]
        count_s[letter] = count_s.get(letter, 0) + 1
        if letter in count_t and count_s[letter] == count_t[letter]:
            have += 1
        while have == need:
            if right - left + 1 < res_len:
                res = [left, right + 1]
                res_len = right - left + 1
            count_s[s[left]] -= 1
            if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                have -= 1
            left += 1
    left, right = res
    return s[left:right] if res_len != float('infinity') else ''
