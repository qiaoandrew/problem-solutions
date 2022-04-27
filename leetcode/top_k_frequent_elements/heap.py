from collections import Counter
import heapq


def top_k_frequent(nums, k):
    if k == len(nums):
        return nums

    occurences_hash_table = Counter(nums)

    return heapq.nlargest(k,
                          occurences_hash_table.keys(),
                          key=occurences_hash_table.get)


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
