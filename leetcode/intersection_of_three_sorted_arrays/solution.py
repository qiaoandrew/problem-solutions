def arrays_intersection(arr1, arr2, arr3):
    p1 = p2 = p3 = 0
    output = 0
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            output.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        else:
            if arr1[p1] < arr2[p2]:
                p1 += 1
            elif arr2[p2] < arr3[p3]:
                p2 += 1
            else:
                p3 += 1
    return output
