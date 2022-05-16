def num_k_len_substr_no_repeats(s, k):
    if k > 26:
        return 0
    characters = {}
    left = 0
    no_repeated_chars = 0
    for right in range(len(s)):
        while s[right] in characters:
            characters[s[left]] -= 1
            if characters[s[left]] == 0:
                characters.pop(s[left])
            left += 1
        characters[s[right]] = 1
        if right - left + 1 == k:
            no_repeated_chars += 1
            characters.pop(s[left])
            left += 1
    return no_repeated_chars


print(
    num_k_len_substr_no_repeats(
        "gdggdbjchgadcfddfahbdebjbagaicgeahehjhdfghadbcbbfhgefcihbcbjjibjdhfhbdijehhiabad",
        5))
