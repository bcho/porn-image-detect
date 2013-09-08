#coding: utf-8

from PIL import Image

from detect import get_ycbcr


def main(name):
    image = Image.open(name)
    ycbcr_image = Image.new('RGB', image.size, 'black')
    ycbcr, pixels = get_ycbcr(image), ycbcr_image.load()

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            pixels[i, j] = tuple(map(int, ycbcr[i * image.size[1] + j]))

    ycbcr_image.show()


if __name__ == '__main__':
    import sys
    main(sys.argv[-1])
