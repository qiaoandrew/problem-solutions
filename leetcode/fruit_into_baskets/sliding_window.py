def total_fruit(fruits):
    left = 0
    max_num = 0
    fruit_freq = {}
    for right in range(len(fruits)):
        fruit_freq[fruits[right]] = fruit_freq.get(fruits[right], 0) + 1
        while len(fruit_freq) > 2:
            fruit_freq[fruits[left]] -= 1
            if fruits.freq[fruits[left]] == 0:
                fruit_freq.pop(fruits[left])
            left += 1
        max_num = max(max_num, right - left + 1)
    return max_num
