def number_of_subarrays(nums, k):
    num_odd = 0
    num_nice = 0
    left = 0
    cur_sub_count = 0
    for right in range(len(nums)):
        if nums[right] % 2 == 1:
            num_odd += 1
            cur_sub_count = 0
        while num_odd == k:
            if nums[left] % 2 == 1:
                num_odd -= 1
            cur_sub_count += 1
            left += 1
        num_nice += cur_sub_count
    return num_nice
