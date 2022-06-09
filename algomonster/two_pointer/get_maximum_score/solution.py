MODULO_AMT = 10**9 + 7


def maximum_score(arr1, arr2):
    p1 = p2 = 0
    result = 0
    section_sum1 = section_sum2 = 0

    while p1 < len(arr1) or p2 < len(arr2):
        if p1 < len(arr1) and p2 < len(arr2) and arr1[p1] == arr2[p2]:
            result += max(section_sum1, section_sum2) + arr1[p1]
            result %= MODULO_AMT
            section_sum1 = section_sum2 = 0
            p1 += 1
            p2 += 1
            continue

        if p1 == len(arr1) or (p2 != len(arr2) and arr1[p1] > arr2[p2]):
            section_sum2 += arr2[p2]
            p2 += 1
        else:
            section_sum1 += arr1[p1]
            p1 += 1

    result += max(section_sum1, section_sum2)
    return result % MODULO_AMT
