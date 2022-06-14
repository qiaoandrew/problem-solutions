import heapq


def nth_ugly_number(n):
    allowed_prime = (2, 3, 5)
    ans_heap = [1]
    used_nums = {1}
    for _ in range(n - 1):
        val = heapq.heappop(ans_heap)
        for multiplier in allowed_prime:
            if val * multiplier not in used_nums:
                heapq.heappush(ans_heap, val * multiplier)
                used_nums.add(val * multiplier)
    return ans_heap[0]
