from collections import Counter
import heapq


def reorganize_string(s):
    res = []
    counts = Counter(s)
    heap = [(-occ, char) for char, occ in counts.items()]
    heapq.heapify(heap)

    while len(heap) > 0:
        if len(res) > 0 and heap[0][1] == res[-1]:
            occ1, char1 = heapq.heappop(heap)
            if len(heap) == 0:
                return ''
            occ2, char2 = heapq.heappop(heap)
            res.append(char2)
            occ2 += 1
            if occ2 < 0:
                heapq.heappush(heap, (occ2, char2))
            heapq.heappush(heap, (occ1, char1))
        else:
            occ1, char1 = heapq.heappop(heap)
            res.append(char1)
            occ1 += 1
            if occ1 < 0:
                heapq.heappush(heap, (occ1, char1))

    return ''.join(res)
