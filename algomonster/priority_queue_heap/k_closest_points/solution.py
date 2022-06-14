from math import sqrt
import heapq


def k_closest_points(points, k):
    min_heap = []
    for point in points:
        heapq.heappush(min_heap, (sqrt(point[0]**2 + point[1]**2), point))

    smallest = []
    for _ in range(k):
        _, point = heapq.heappop(min_heap)
        smallest.append(point)

    return smallest