from PIL import Image
import random
import math

# dimension of the image X * X
image_dimensionX = 720
image_dimensionY = 1280

# initial brightness of the image
image_brightness = 100

# Color 1 for Gradient
color_one = [150, 180, 190]

# Color 2 for Gradient
color_two = [190, 100, 120]

# Change Color From Which Point ( 0.5 means half )
image_change_range = 0.5


def randomPixel():
    return random.randint(1, 255)


def purify_pixel():
    r = randomPixel()
    g = randomPixel()
    b = randomPixel()

    # This is by perceived option 1
    current_brightness = 0.299 * r + 0.587 * g + 0.114 * b

    ratio_rg = color_one[0] / color_one[1]
    ratio_rb = color_one[0] / color_one[2]
    ratio_gb = color_one[1] / color_one[2]

    current_ratio_rg = r / g
    current_ratio_rb = r / b
    current_ratio_gb = g / b

    while (current_brightness < image_brightness - 20 or current_brightness > image_brightness + 20) or (
            current_ratio_rg < ratio_rg - 0.8 or current_ratio_rg > ratio_rg + 0.8) or (
            current_ratio_rb < ratio_rb - 0.8 or current_ratio_rb > ratio_rb + 0.8) or (
            current_ratio_gb < ratio_gb - 0.8 or current_ratio_gb > ratio_gb + 0.8):

        r = randomPixel()
        g = randomPixel()
        b = randomPixel()

        current_ratio_rg = r / g
        current_ratio_rb = r / b
        current_ratio_gb = g / b
        current_brightness = 0.299 * r + 0.587 * g + 0.114 * b

    return [r, g, b]


def newImg():
    global image_brightness
    global color_one
    global blank
    temp = color_one
    brightness_increase_factor = (250 - image_brightness)/(image_dimensionX * (image_change_range - 0.1))
    # brightness_increase_factor = 5
    switch = True

    img = Image.new('RGB', (image_dimensionX, image_dimensionY))
    i = 1
    j = 1
    while i < image_dimensionX:
        j = 1
        while j < image_dimensionY:
            rgb = purify_pixel()
            img.putpixel((i, j), (rgb[0], rgb[1], rgb[2]))
            print(i, j)
            j += 1

        i += 1

        if switch and image_brightness < 250:
            image_brightness += brightness_increase_factor
        else:
            switch = False
            color_one = color_two
        if not switch and image_brightness > 5:
            image_brightness -= brightness_increase_factor
        else:
            switch = True
            color_one = temp

    img.save('sqr.png')
    return img


wallpaper = newImg()
wallpaper.show()
