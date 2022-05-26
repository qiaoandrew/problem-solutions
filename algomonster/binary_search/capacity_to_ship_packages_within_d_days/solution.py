def min_max_weight(weights, d):
    min_weight = max(weights)
    max_weight = sum(weights)
    ideal_weight = max_weight
    while min_weight <= max_weight:
        mid_weight = (min_weight + max_weight) // 2
        if feasible(weights, d, mid_weight):
            ideal_weight = mid_weight
            max_weight = mid_weight - 1
        else:
            min_weight = mid_weight + 1
    return ideal_weight


def feasible(weights, d, max_weight):
    required_days = 1
    capacity_left = max_weight
    i = 0
    while i < len(weights):
        if capacity_left >= weights[i]:
            capacity_left -= weights[i]
            i += 1
        else:
            required_days += 1
            capacity_left = max_weight
    return required_days <= d