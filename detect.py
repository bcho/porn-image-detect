#coding: utf-8

from PIL import Image

SIZE = 150, 150
THRESHOLD = 0.5


def prepare_image(image):
    if not image.mode == 'RGB':
        image = image.convert(mode='RGB')
    image.thumbnail(SIZE, Image.ANTIALIAS)
    return image


def get_ycbcr(image):
    ret = []

    def rgb2ycbcr(r, g, b):
        return (
            16 + (65.738 * r + 129.057 * g + 25.064 * b) / 256,
            128 + (-37.945 * r - 74.494 * g + 112.439 * b) / 256,
            128 + (112.439 * r - 94.154 * g - 18.285 * b) / 256
        )

    x, y = image.size
    for i in range(0, x):
        for j in range(0, y):
            ret.append(rgb2ycbcr(*image.getpixel((i, j))))

    return ret


def detect(image):

    def judge(sample):
        y, cb, cr = sample

        return 80 <= cb <= 120 and 133 <= cr <= 173

    image = prepare_image(image)
    ycbcr = get_ycbcr(image)

    judged = map(judge, ycbcr)

    rating = float(judged.count(True)) / len(judged)
    return rating > THRESHOLD, rating


if __name__ == '__main__':
    import sys
    print sys.argv[-1]
    image = Image.open(sys.argv[-1])
    print detect(image)
