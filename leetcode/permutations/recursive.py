def permute(nums):
    result = []
    generate_permutations(nums, 0, [], result)
    return result


def generate_permutations(nums, index, cur_permutation, result):
    if index == len(nums):
        result.append(cur_permutation)
    else:
        for i in range(len(cur_permutation) + 1):
            new_permutation = list(cur_permutation)
            new_permutation.insert(i, nums[index])
            generate_permutations(nums, index + 1, new_permutation, result)
