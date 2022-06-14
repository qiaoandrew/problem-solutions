import heapq


class MedianOfStream:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_number(self, num):
        if len(self.min_heap) == 0 or num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self._balance()

    def get_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        return -self.max_heap[0]

    def _balance(self):
        if len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
