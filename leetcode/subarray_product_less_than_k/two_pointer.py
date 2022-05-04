def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    left = 0
    ans = 0
    cur_product = 1
    for right in range(len(nums)):
        cur_product *= nums[right]
        while cur_product >= k:
            cur_product /= nums[left]
            left += 1
        ans += right - left + 1
    return ans
