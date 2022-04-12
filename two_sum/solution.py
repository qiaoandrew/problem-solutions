def two_sum(arr, target_sum):
    if len(arr) <= 1: return None
    hash_map = {}
    for i, num in enumerate(arr):
        target_num = target_sum - num
        if target_num in hash_map:
            return [i, hash_map[target_num]]
        else:
            hash_map[num] = i
    return None


print(two_sum([2, 7, 11, 15], 22))