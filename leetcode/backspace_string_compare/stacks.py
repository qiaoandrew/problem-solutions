def backspace_string_compare(s, t):

    def createStack(string):
        stack = []
        for letter in string:
            if letter != '#':
                stack.append(letter)
            elif len(stack) > 0:
                stack.pop()
        return stack

    return createStack(s) == createStack(t)


print(backspace_string_compare('##', '##'))