def min_window(s, t):
    if t == '' or len(t) > len(s):
        return ''
    s_letters, t_letters = {}, {}
    for letter in t:
        t_letters[letter] = t_letters.get(letter, 0) + 1
    have, need = 0, len(t_letters)
    result, result_len = [-1, -1], float('inf')
    left = 0
    for right in range(len(s)):
        cur_letter = s[right]
        s_letters[cur_letter] = s_letters.get(cur_letter, 0) + 1
        if cur_letter in t_letters and s_letters[cur_letter] == t_letters[
                cur_letter]:
            have += 1
        while have == need:
            if right - left + 1 < result_len:
                result = [left, right + 1]
                result_len = right - left + 1
            s_letters[s[left]] -= 1
            if s[left] in t_letters and s_letters[s[left]] < t_letters[
                    s[left]]:
                have -= 1
            left += 1
    left, right = result
    return s[left:right] if result_len != float('inf') else ''
