def merge_sorted_array(nums1, m, nums2, n):
    pointer_1 = m - 1
    pointer_2 = n - 1
    for i in range(len(nums1) - 1, -1, -1):
        if pointer_1 >= 0 and pointer_2 >= 0:
            if nums1[pointer_1] > nums2[pointer_2]:
                nums1[i] = nums1[pointer_1]
                pointer_1 -= 1
            else:
                nums1[i] = nums2[pointer_2]
                pointer_2 -= 1
        elif pointer_1 >= 0:
            nums1[i] = nums1[pointer_1]
            pointer_1 -= 1
        else:
            nums1[i] = nums2[pointer_2]
            pointer_2 -= 1
    return nums1


print(merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
