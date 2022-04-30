def ship_within_days(weights, days):
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        days_needed = 1
        cur_weight = 0
        for weight in weights:
            if cur_weight + weight > mid:
                days_needed += 1
                cur_weight = 0
            cur_weight += weight
        if days_needed > days:
            left = mid + 1
        else:
            right = mid
    return left


print(ship_within_days([1, 2, 3, 1, 1], 4))
