def interval_intersection(first_list, second_list):
    ans = []
    i = j = 0
    while i < len(first_list) and j < len(second_list):
        low = max(first_list[i][0], second_list[j][0])
        high = min(first_list[i][1], second_list[j][1])
        if low <= high:
            ans.append([low, high])
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    return ans
