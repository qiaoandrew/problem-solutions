def sort_sentence(s):
    words = s.split()
    positions = {}
    for word in words:
        positions[int(word[-1])] = word[:-1]
    result = ''
    for i in range(1, len(words) + 1):
        result += positions[i]
        result += ' '
    return result.rstrip()


print(sort_sentence('is2 sentence4 This1 a3'))
