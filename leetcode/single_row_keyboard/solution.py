def calculate_time(keyboard, word):
    positions = {}
    for i in range(len(word)):
        positions[word[i]] = i
    time = 0
    for i in range(len(word) - 1):
        time += abs(positions[i + 1] - positions[i])
    return time
