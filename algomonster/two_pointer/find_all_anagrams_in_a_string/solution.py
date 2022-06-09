def find_all_anagrams(original, check):
    check_count = {}
    for c in check:
        check_count[c] = check_count.get(c, 0) + 1

    indices = []
    count = {}
    left = 0

    for right in range(len(original)):
        count[original[right]] = count.get(original[right], 0) + 1

        if right - left + 1 == len(check):
            if count == check_count:
                indices.append(left)
            count[original[left]] -= 1
            if count[original[left]] == 0:
                count.pop(original[left])
            left += 1
    return indices
