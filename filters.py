# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
import math

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    im = Image.open(filename)
    return im


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(im):
    im.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(im, filename):
    im.save(filename, "jpeg")
    show_img(im)

# Define your obamicon() function here.
#Parameters: The image object to apply the filter to.
#Returns: A New Image object with the filter applied.
def obamicon(im):
#load the pixel data from im
    pixels = im.getdata()
#create ls to hold new image pixel data
    new_pixel = []
#define color constants (3-tuple) tp use for recoloring
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    #process the pixels in the Image
    for p in pixels:
        #pixel intensity = R + G + B
        intensity = p[0] + p[1] + p[2]

        #replace existing pixels with new pixel colors based on their intensity
        if intensity < 182:
            new_pixel.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            new_pixel.append(red)
        elif intensity >= 364 and intensity < 546:
            new_pixel.append(lightBlue)
        else:
            new_pixel.append(yellow)
        #save the pixel to the new_pixel list
    recolored = Image.new("RGB", im.size)
    recolored.putdata(new_pixel)
    return recolored

def grayscale(im):
    pixels = im.getdata()
#create ls to hold new image pixel data
    new_pixel = []
#define color constants (3-tuple) tp use for recoloring
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Gray = (128, 128, 128)
    LGray = (192, 192, 192)
    #process the pixels in the Image
    for p in pixels:
        #pixel intensity = R + G + B
        intensity = p[0] + p[1] + p[2]

        #replace existing pixels with new pixel colors based on their intensity
        if intensity < 182:
            new_pixel.append(Black)
        elif intensity >= 182 and intensity <= 350:
            new_pixel.append(Gray)
        elif intensity >= 350 and intensity <=560:
            new_pixel.append(LGray)
        else:
            new_pixel.append(White)

        #save the pixel to the new_pixel list
    recolored = Image.new("RGB", im.size)
    recolored.putdata(new_pixel)
    return recolored

def purple(im):
    pixels = im.getdata()
#create ls to hold new image pixel data
    new_pixel = []
#define color constants (3-tuple) tp use for recoloring
    pDark = (42, 0, 74)
    Dark = (135, 71, 157)
    Purple = (206, 132, 225)
    Light = (231, 213, 249)
    pLight = (247, 227, 253)
    #process the pixels in the Image
    for p in pixels:
        #pixel intensity = R + G + B
        intensity = p[0] + p[1] + p[2]

        #replace existing pixels with new pixel colors based on their intensity
        if intensity < 200:
            new_pixel.append(pDark)
        elif intensity >= 200 and intensity <= 350:
            new_pixel.append(Dark)
        elif intensity >= 350 and intensity <= 450:
            new_pixel.append(Purple)
        elif intensity >= 450 and intensity <= 550:
            new_pixel.append(Light)
        else:
            new_pixel.append(pLight)

        #save the pixel to the new_pixel list
    recolored = Image.new("RGB", im.size)
    recolored.putdata(new_pixel)
    return recolored
