def top_k_frequent(nums, k):
    count = {}
    frequencies = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num, occurences in count.items():
        frequencies[occurences].append(num)

    res = []
    for occurences in range(len(frequencies) - 1, 0, -1):
        for num in frequencies[occurences]:
            res.append(num)
            if len(res) == k:
                return res


print(top_k_frequent([3, 0, 1, 0], 1))
