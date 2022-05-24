from collections import deque


def permute(nums):
    result = []
    permutations = deque([[]])

    for num in nums:
        n = len(permutations)

        for _ in range(n):
            old_permutation = permutations.popleft()

            for i in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(i, num)
                if len(new_permutation) == len(nums):
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)

    return result
