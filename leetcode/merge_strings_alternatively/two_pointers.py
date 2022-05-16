def merge_alternatively(word1, word2):
    result = ''
    pointer_1, pointer_2 = 0, 0
    while pointer_1 < len(word1) or pointer_2 < len(word2):
        if pointer_1 == len(word1):
            result += word2[pointer_2]
            pointer_2 += 1
        elif pointer_2 == len(word2):
            result += word1[pointer_1]
            pointer_1 += 1
        else:
            if pointer_1 != pointer_2:
                result += word2[pointer_2]
                pointer_2 += 1
            else:
                result += word1[pointer_1]
                pointer_1 += 1
    return result