import math


def min_sub_array_len(target, nums):
    length = len(nums)
    ans = math.inf

    # Loop through every possible sub array using two pointers
    for i in range(length):
        for j in range(i, length):
            # Calculate the sum of the sub array
            sub_sum = 0
            for num in nums[i:j + 1]:
                sub_sum += num
            # Change the answer if the sum is greater than the target
            # and the number of elements is smaller than the current answer
            if sub_sum >= target:
                ans = min(ans, j - i + 1)
    return 0 if ans == math.inf else ans


print(min_sub_array_len(20, [1, 4, 4]))
