def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix_length = 0
    for i in range(len(min(strs))):
        cur_letter = strs[0][i]
        for string in strs:
            if string[i] != cur_letter:
                return strs[0][:prefix_length]
        prefix_length += 1

    return strs[0][:prefix_length]
