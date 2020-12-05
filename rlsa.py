from numpy import ndarray


def iteration(image: ndarray, value: int) -> ndarray:
    rows, cols = image.shape
    for row in range(0, rows):
        try:
            begin = image[row].tolist().index(0)
        except ValueError:
            begin = 0

        count = begin
        for col in range(begin, cols):
            if image[row, col] == 0:
                if(col - count) <= value and (col-count) > 0:
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

