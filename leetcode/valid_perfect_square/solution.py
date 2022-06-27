def is_perfect_square(num):
    left, right = 1, num
    while left <= right:
        mid = (left + right) // 2
        square = mid**2
        if square == num:
            return mid
        elif square > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1
