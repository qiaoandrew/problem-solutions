def search(nums, target):

    def binary_search(nums, target, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search(nums, target, start, end - 1)
        else:
            return binary_search(nums, target, mid + 1, end)

    return binary_search(nums, target, 0, len(nums) - 1)
