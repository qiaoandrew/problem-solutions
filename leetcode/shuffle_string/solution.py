def restore_string(s, indices):
    result = [''] * len(indices)
    for index, char in enumerate(s):
        result[indices[index]] = char
    return ''.join(result)
