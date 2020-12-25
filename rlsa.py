from numpy import ndarray, arange, nditer


def iteration(image: ndarray, value: int) -> ndarray:
    for row in nditer(arange(image.shape[0])):
        try:
            begin = image[row].tolist().index(0)
        except ValueError:
            begin = 0
            count = begin

    for col in nditer(arange(begin, image.shape[1])):
        if image[row, col] == 0:
            if value >= (col - count) > 0:
                image[row, count:col] = 0
                count = col
    return image


def rlsa(image: ndarray, horizontal: bool = True, vertical: bool = True, value: int = 0) -> ndarray:
    if isinstance(image, ndarray):
        if value >= 0:
            value = int(value)
        else:
            value = 0
        try:
            if horizontal:
                image = iteration(image, value)
            if vertical:
                image = image.T
                image = iteration(image, value)
                image = image.T

        except (AttributeError, ValueError) as e:
            image = None
            print("Error: ", e, "\n")

    else:
        print('Image has to be as numpy ndarray and binary')
        image = None
    return image

