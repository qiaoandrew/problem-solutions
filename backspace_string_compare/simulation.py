def backspace_compare(s, t):

    def get_next_char(string, pointer):
        char, skip_count = '', 0
        while pointer >= 0 and not char:
            if string[pointer] == '#':
                skip_count += 1
            elif skip_count > 0:
                skip_count -= 1
            else:
                char = string[pointer]
            pointer -= 1
        return char, pointer

    pointer_s, pointer_t = len(s) - 1, len(t) - 1
    while pointer_s >= 0 or pointer_t >= 0:
        char_s = char_t = ''
        if pointer_s >= 0:
            char_s, pointer_s = get_next_char(s, pointer_s)
        if pointer_t >= 0:
            char_t, pointer_t = get_next_char(t, pointer_t)
        if char_s != char_t:
            return False
    return True