def backspace_string_compare(s, t):
    listS = []
    listT = []
    for i in range(len(s)):
        if s[i] == '#':
            if listS:
                listS.pop()
        elif not s[i] == '#':
            listS.append(s[i])
    for i in range(len(t)):
        if t[i] == '#':
            if listT:
                listT.pop()
        elif not t[i] == '#':
            listT.append(t[i])
    return (listS == listT)


print(backspace_string_compare('##', '##'))