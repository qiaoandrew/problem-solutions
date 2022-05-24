def balance_string_split(s):
    cur_l = 0
    cur_r = 0
    splits = 0

    for char in s:
        if char == 'L':
            cur_l += 1
        if char == 'R':
            cur_r += 1
        if cur_l == cur_r:
            splits += 1
            cur_l = cur_r = 0

    return splits