def subarray_sum(nums, k):
    slow = 0
    cur_sum = 0
    subarrays = 0
    for fast in range(len(nums)):
        cur_sum += nums[fast]
        if cur_sum == k:
            subarrays += 1
        while cur_sum >= k:
            cur_sum -= nums[slow]
            slow += 1
    return subarrays
