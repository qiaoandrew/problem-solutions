def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    used_rooms = 0
    start_times = sorted(i[0] for i in intervals)
    end_times = sorted(i[1] for i in intervals)
    start_pointer, end_pointer = 0, 0
    while start_pointer < len(intervals):
        if start_times[start_pointer] >= end_times[end_pointer]:
            used_rooms -= 1
            end_pointer += 1
        used_rooms += 1
        start_pointer += 1
    return used_rooms
