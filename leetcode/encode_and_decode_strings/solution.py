def encode(strs):
    code = ''
    for string in strs:
        code += (str(len(string)) + '#' + string)
    return code


def decode(s):
    strs, i = [], 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        strs.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return strs


print(decode('5#hello5#world'))