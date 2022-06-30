def rotate(nums, k):
    n = len(nums)
    k %= n

    start_index = num_replacements = 0
    while num_replacements < n:
        cur_index, prev_num = start_index, nums[start_index]
        while True:
            next_index = (cur_index + k) % n
            nums[next_index], prev_num = prev_num, nums[next_index]
            cur_index = next_index
            num_replacements += 1

            if start_index == cur_index:
                break
        start_index += 1
