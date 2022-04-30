def square_root(n):
    if n == 0:
        return 0
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if mid**2 > n:
            right = mid - 1
        else:
            index = mid
            left = mid + 1
    return index
