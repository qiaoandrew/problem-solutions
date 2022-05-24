def number_of_substrings(s):
    num_substrings = 0
    left = 0
    counter = {c: 0 for c in 'abc'}
    for right in range(len(s)):
        counter[s[right]] += 1
        while all(counter.values()):
            counter[s[left]] -= 1
            left += 1
        num_substrings += left
    return num_substrings
