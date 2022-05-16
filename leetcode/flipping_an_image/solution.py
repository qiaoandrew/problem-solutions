def flip_and_invert_image(image):
    result = []
    for row in image:
        invert = lambda x: 0 if x == 1 else 1
        result.append(list(map(invert, row[::-1])))
    return result
