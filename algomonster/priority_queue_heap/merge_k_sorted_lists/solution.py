import heapq


def merge_k_sorted_list(lists):
    min_heap = []
    for cur_list in lists:
        heapq.heappush(min_heap, (cur_list[0], cur_list, 0))

    res = []
    while len(min_heap) > 0:
        val, cur_list, index = heapq.heappop(min_heap)
        res.append(val)
        index += 1
        if index < len(cur_list):
            heapq.heappush(min_heap, (cur_list[index], cur_list, index))
    return res