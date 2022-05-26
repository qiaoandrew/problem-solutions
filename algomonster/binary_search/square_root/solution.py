def square_root(n):
    if n == 0:
        return 0
    start, end = 1, n
    index = -1
    while start <= end:
        mid = (start + end) // 2
        if mid**2 > n:
            end = mid - 1
        else:
            index = mid
            start = mid + 1
    return index
