def get_minimum_window(original, check):
    check_count = {}
    for c in check:
        check_count[c] = check_count.get(c, 0) + 1
    conditions = len(check_count)

    count = {}
    conditions_met = 0
    min_length = float('inf')
    min_left, min_right = -1, -1
    left = 0
    for right in range(len(original)):
        if original[right] in check_count:
            count[original[right]] = count.get(original[right], 0) + 1
            if count[original[right]] == check_count[original[right]]:
                conditions_met += 1

        while conditions_met == conditions:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
                min_right = right
            elif right - left + 1 == min_length:
                if original[left:right + 1] < original[min_left:min_right + 1]:
                    min_left = left
                    min_right = right

            if original[left] in check_count:
                count[original[left]] -= 1
                if count[original[left]] < check_count[original[left]]:
                    conditions_met -= 1
            left += 1

    return original[min_left:min_right +
                    1] if min_left != -1 and min_right != -1 else ''
