def next_greatest_letter(letters, target):
    if (ord(target) >= ord(letters[-1])):
        return letters[0]
    left, right = 0, len(letters) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if ord(letters[mid]) > ord(target):
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return letters[index]


print(next_greatest_letter(["a", "b"], 'z'))
