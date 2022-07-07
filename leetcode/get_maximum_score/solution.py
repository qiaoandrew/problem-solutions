def max_sum(nums1, nums2):
    result = 0
    p1 = p2 = 0
    n1, n2 = len(nums1), len(nums2)
    section_sum1 = section_sum2 = 0
    MODULO_AMT = 10**9 + 7

    while p1 < n1 or p2 < n2:
        if p1 < n1 and p2 < n2 and nums1[p1] == nums2[p2]:
            result += max(section_sum1, section_sum2) + nums1[p1]
            result %= MODULO_AMT
            section_sum1 = 0
            section_sum2 = 0
            p1 += 1
            p2 += 1
        elif p1 == n1 or (p2 != n2 and nums1[p1] > nums2[p2]):
            section_sum2 += nums2[p2]
            p2 += 1
        else:
            section_sum1 += nums1[p1]
            p1 += 1

    result += max(section_sum1, section_sum2)
    return result % MODULO_AMT