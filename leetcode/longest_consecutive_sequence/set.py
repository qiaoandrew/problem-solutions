def longest_consecutive(nums):
    nums_set = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in nums_set:
            cur_longest = 1
            while num + 1 in nums_set:
                cur_longest += 1
                num += 1
            longest = max(longest, cur_longest)
    return longest