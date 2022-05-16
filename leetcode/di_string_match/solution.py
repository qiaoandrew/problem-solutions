def di_string_match(s):
    low, high = 0, len(s)
    result = []
    exit_condition = False
    i = 0
    while i < len(s):
        if s[i] == 'I':
            result.append(low)
            low += 1
        elif s[i] == 'D':
            result.append(high)
            high -= 1
        if i == len(s) - 1:
            if not exit_condition:
                i -= 1
            exit_condition = True
        i += 1
    return result
