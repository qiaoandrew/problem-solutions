from collections import defaultdict


def four_sum_count(nums1, nums2, nums3, nums4):
    count = 0
    sums = defaultdict(int)
    for num1 in nums1:
        for num2 in nums2:
            sums[num1 + num2] += 1

    for num3 in nums3:
        for num4 in nums4:
            count += sums(-(num3 + num4))

    return count