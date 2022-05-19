def num_jewels_in_stones(jewels, stones):
    jewel_types = set()
    jewel_num = 0
    for jewel in jewels:
        jewel_types.add(jewel)
    for stone in stones:
        if stone in jewel_types:
            jewel_num += 1
    return jewel_num
