def decompress_rle_list(nums):
    decompressed = []
    for i in range(0, len(nums), 2):
        decompressed += [nums[i + 1] for _ in range(nums[i])]
    return decompressed
