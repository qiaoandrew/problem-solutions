from collections import deque


def num_steps(target_combo, trapped_combos):

    def get_changes(num):
        changes = []
        for i in range(4):
            next_digit = int(num[i]) + 1
            if next_digit > 9:
                next_digit = 0
            next_num = num[:i] + str(next_digit) + num[i + 1:]
            changes.append(str(next_num))

            prev_digit = int(num[i]) - 1
            if prev_digit < 0:
                prev_digit = 9
            prev_num = num[:i] + str(prev_digit) + num[i + 1:]
            changes.append(str(prev_num))
        return changes

    if target_combo == '0000':
        return 0

    queue = deque(['0000'])
    traps = set(trapped_combos)
    visited = set(['0000'])
    changes = 0

    while len(queue) > 0:
        num_changes = len(queue)
        for _ in range(num_changes):
            combo = queue.popleft()
            if combo == target_combo:
                return changes

            for change in get_changes(combo):
                if change in visited or change in traps:
                    continue
                queue.append(change)
                visited.add(change)
        changes += 1

    return -1