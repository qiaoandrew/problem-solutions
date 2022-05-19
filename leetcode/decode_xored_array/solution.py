def decode(encoded, first):
    decoded = [first]
    for num in encoded:
        decode.append(decoded[-1] ^ num)
    return decoded
