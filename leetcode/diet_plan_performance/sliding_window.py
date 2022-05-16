def diet_plan_performance(calories, k, lower, upper):
    cur_sum = 0
    left = 0
    points = 0
    for right in range(len(calories)):
        cur_sum += calories[right]
        if right - left + 1 == k:
            if cur_sum > upper:
                points += 1
            elif cur_sum < lower:
                points -= 1
            cur_sum -= calories[left]
            left += 1
    return points
