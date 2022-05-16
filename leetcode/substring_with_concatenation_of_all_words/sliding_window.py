def find_substring(s, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    result_indices = []
    words_count = len(words)
    word_length = len(words[0])
    for i in range((len(s) - words_count * word_length) + 1):
        words_seen = {}
        for j in range(words_count):
            next_word_index = i + j * word_length
            word = s[next_word_index:next_word_index + word_length]
            if word not in word_frequency:
                break
            words_seen[word] = words_seen.get(word, 0) + 1
            if words_seen[word] > word_frequency.get(word, 0):
                break
            if j + 1 == words_count:
                result_indices.append(i)
    return result_indices
