from heapq import *
import heapq


class SlidingWindowMedia:

    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def median_sliding_window(self, nums, k):
        result = [0.0 for _ in range(len(nums) - k + 1)]

        for i in range(len(nums)):
            if not self.max_heap or nums[i] <= -self.max_heap[0]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])

            self.rebalance_heaps()

            if i >= k - 1:
                if len(self.max_heap) == len(self.min_heap):
                    result[i - k +
                           1] = (-self.max_heap[0] + self.min_heap[0]) / 2.0
                else:
                    result[i - k + 1] = -self.max_heap[0]

                element_to_be_removed = nums[i - k + 1]
                if element_to_be_removed <= -self.max_heap[0]:
                    self.remove(self.max_heap, -element_to_be_removed)
                else:
                    self.remove(self.min_heap, element_to_be_removed)

            self.rebalance_heaps()

        return result

    def remove(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        del heap[-1]
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
