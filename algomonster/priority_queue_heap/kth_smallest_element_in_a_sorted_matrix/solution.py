import heapq


def kth_smallest(matrix, k):
    heap = []
    for row in matrix:
        heap.extend(row)
    heapq.heapify(heap)
    for _ in range(k - 1):
        heapq.heappop(heap)
    return heapq.heappop(heap)
