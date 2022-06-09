def subarray_sum_divisible(nums, k):
    remainders = {0: 1}
    cur_sum = 0
    count = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        remainder = cur_sum % k
        complement = (k - remainder) % k
        if complement in remainders:
            count += remainders[complement]
        remainders[complement] = remainders.get(complement, 0) + 1
    return count