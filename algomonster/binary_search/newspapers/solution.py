def newspaper_split(newspapers, coworkers):
    low, high = 0, 10000000001
    index = -1
    while low <= high:
        mid = (low + high) // 2
        if feasible(newspapers, coworkers, mid):
            index = mid
            high = mid - 1
        else:
            low = mid = 1
    return index


def feasible(newspapers, coworkers, time):
    coworkers_needed = 1
    cur_time = time
    i = 0
    while i < len(newspapers):
        if newspapers[i] > time:
            return False
        if cur_time >= newspapers[i]:
            cur_time -= newspapers[i]
            i += 1
        else:
            coworkers_needed += 1
            cur_time = time
    return coworkers_needed <= coworkers
