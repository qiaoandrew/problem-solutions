# 1. Find index of highest number using binary search
# 2. Do binary search on increasing part
# 3. If found number, return index
# 4. If not found number, binary search decreasing part


def find_in_mountain_array(target, mountain_arr):
    left, right = 0, mountain_arr.length() - 1
    while left < right:
        mid = (left + right) // 2
        if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
            left = mid + 1
        else:
            right = mid
    peak = left

    left, right = 0, peak
    while left <= right:
        mid = (left + right) // 2
        if mountain_arr.get(mid) < target:
            left = mid + 1
        elif mountain_arr.get(mid) > target:
            right = mid - 1
        else:
            return mid

    left, right = peak, mountain_arr.length() - 1
    while left <= right:
        mid = (left + right) // 2
        if mountain_arr.get(mid) > target:
            left = mid + 1
        elif mountain_arr.get(mid) < target:
            right = mid - 1
        else:
            return mid

    return -1