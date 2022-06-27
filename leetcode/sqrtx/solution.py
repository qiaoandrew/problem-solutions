def mySqrt(self, x: int) -> int:
    low, high = 0, x
    possible_root = -1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            possible_root = mid
            low = mid + 1
        else:
            high = mid - 1
    return possible_root
