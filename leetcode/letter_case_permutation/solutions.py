def letter_case_permutation(s):
    permutations = [s]
    for i in range(len(s)):
        if s[i].isalpha():
            n = len(permutations)
            for j in range(n):
                cur_permutation_characters = list(permutations[j])
                cur_permutation_characters[i] = cur_permutation_characters[
                    i].swapcase()
                permutations.append(' '.join(cur_permutation_characters))
    return permutations
