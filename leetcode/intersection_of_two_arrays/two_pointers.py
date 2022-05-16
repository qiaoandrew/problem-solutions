def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = []
    pointer1, pointer2 = 0, 0
    while pointer1 < len(nums1) and pointer2 < len(nums2):
        num1, num2 = nums1[pointer1], nums2[pointer2]
        if num1 == num2:
            result.append(num1)
            while num1 == nums1[pointer1]:
                pointer1 += 1
                if pointer1 == len(nums1):
                    break
            while num2 == nums2[pointer2]:
                pointer2 += 1
                if pointer2 == len(nums2):
                    break
        elif num1 > num2:
            pointer2 += 1
        else:
            pointer1 += 1
    return result


print(intersection([1, 2, 2, 1], [2, 2]))
