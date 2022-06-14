import heapq


def find_kth_largest(nums, k):
    nums = [-num for num in nums]
    heapq.heapify(nums)

    for _ in range(k - 1):
        heapq.heappop(nums)
    return -nums[0]
