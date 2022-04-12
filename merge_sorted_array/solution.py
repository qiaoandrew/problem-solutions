def merge(nums1, m, nums2, n):
    p_1 = 0
    p_2 = 0
    nums1_copy = nums1[:m]

    for p in range(m + n):
        if p_2 >= n or (p_1 < m and nums1_copy[p_1] <= nums2[p_2]):
            nums1[p] = nums1_copy[p_1]
            p_1 += 1
        else:
            nums1[p] = nums2[p_2]
            p_2 += 1

    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
