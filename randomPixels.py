from PIL import Image
import random
import math

image_dimension = 500
image_brightness = 150
percentage_rgb = [150, 50, 50]


def randomPixel():
    return random.randint(1, 255)


def purify_pixel():

    rgb = brightness()




    return rgb


def brightness():
    r = randomPixel()
    g = randomPixel()
    b = randomPixel()

    # This is by standard formula
    # current_brightness = 0.21*r + 0.71*g + 0.07*b

    # This is by perceived option 1
    current_brightness = 0.299 * r + 0.587 * g + 0.114 * b

    # This is by perceived option 2 (slower)
    # current_brightness = 0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b)
    # current_brightness = math.sqrt(current_brightness)
    while current_brightness > image_brightness + 10 or current_brightness < image_brightness - 10:
        r = randomPixel()
        g = randomPixel()
        b = randomPixel()

        current_brightness = 0.299 * r + 0.587 * g + 0.114 * b
    return [r, g, b]


def newImg():
    img = Image.new('RGB', (image_dimension, image_dimension))
    i = 1
    j = 1
    while i < image_dimension:
        j = 1
        while j < image_dimension:
            rgb = purify_pixel()
            img.putpixel((i, j), (rgb[0], rgb[1], rgb[2]))
            print(i, j)
            j += 1
        i += 1
    img.save('sqr.png')
    return img


wallpaper = newImg()
wallpaper.show()
