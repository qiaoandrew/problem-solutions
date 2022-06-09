from collections import deque
from string import ascii_letters


def word_ladder(begin, end, word_list):
    words = set(word_list)

    def get_neighbours(word):
        neighbours = []
        for i in range(len(word)):
            for c in ascii_letters:
                neighbour = word[:i] + c + word[i + 1:]
                if neighbour in words:
                    neighbours.append(neighbour)
                    queue.append(neighbour)
                    words.remove(neighbour)
        return neighbours

    queue = deque([begin])
    moves = 0

    while len(queue) > 0:
        num_moves = len(queue)
        for _ in range(num_moves):
            word = queue.popleft()
            for neighbour in get_neighbours(word):
                if neighbour == end:
                    return moves + 1
        moves += 1

    return 0