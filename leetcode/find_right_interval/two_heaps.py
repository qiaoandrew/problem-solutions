from heapq import *


def find_right_interval(intervals):
    max_start_heap = []
    max_end_heap = []
    result = [0 for _ in range(len(intervals))]

    for i in range(len(intervals)):
        heappush(max_start_heap, (-intervals[i][0], i))
        heappush(max_end_heap, (-intervals[i][1], i))

    for _ in range(len(intervals)):
        end, i = heappop(max_end_heap)
        result[i] = -1
        if -max_start_heap[0][0] >= -end:
            start, j = heappop(max_start_heap)
            while max_start_heap and -max_start_heap[0][0] >= -end:
                start, j = heappop(max_start_heap)
            result[i] = j
            heappush(max_start_heap, (start, j))

    return result