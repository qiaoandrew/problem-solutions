import itertools


def backspace_string_compare(s, t):

    def get_letter(str):
        skip = 0
        for x in reversed(str):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

    return all(x == y
               for x, y in itertools.zip_longest(get_letter(s), get_letter(t)))


print(backspace_string_compare('##', '##'))