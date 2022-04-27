def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        cur_sum = numbers[left] + numbers[right]
        if cur_sum == target:
            return [left + 1, right + 1]
        elif cur_sum > target:
            right -= 1
        else:
            left += 1
