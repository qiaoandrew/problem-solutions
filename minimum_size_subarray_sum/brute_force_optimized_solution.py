import math


def min_sub_array_len(target, nums):
    length = len(nums)
    ans = math.inf
    # Create array to store the sums of nums array
    # from index 0 to the number at the same index
    sums = [0] * length
    sums[0] = nums[0]
    # Calculate the sums for the sums array
    for i in range(1, length):
        sums[i] = sums[i - 1] + nums[i]
    # Calculate the sum of each subarray
    # Update answer accordingly
    for i in range(0, length):
        for j in range(i, length):
            sub_sum = sums[j] - sums[i] + nums[i]
            if sub_sum >= target:
                ans = min(ans, j - i + 1)
    return 0 if ans == math.inf else ans


print(min_sub_array_len(5, [1, 4, 4]))
