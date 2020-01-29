import filters

def main():

    filename = input("Enter the name of the image file to edit: ")
    img = filters.load_img(filename)
    filters.save_img(img, "newPic1.jpg")

    print("'O'bamicon, 'G'rayscale, 'P'urple?")
    while True:
        user_input = input()
        if user_input == "O":
            newimg = filters.obamicon(img)
            filters.save_img(newimg, "recolored.jpg")
            break
        if user_input == "G":
            newimg = filters.grayscale(img)
            filters.save_img(newimg, "recolored.jpg")
            break
        if user_input == "P":
            newimg = filters.purple(img)
            filters.save_img(newimg, "recolored.jpg")
            break


if __name__ == '__main__':
        main()
