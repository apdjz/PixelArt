from PIL import Image

# function to pixelate image
def pixelate(image, percent):
    # calculate pixel size based on percent
    width, height = image.size
    pixel_size = int((width + height) * percent / 200)

    # create pixelated image
    pixelated = image.resize((int(width/pixel_size), int(height/pixel_size)), resample=Image.NEAREST)
    pixelated = pixelated.resize((width, height), resample=Image.NEAREST)

    return pixelated

# get input image file from user
filename = input("Enter the path to the image file you want to pixelate: ")

# open image and get user input for pixelation percentage
try:
    with Image.open(filename) as image:
        percent = float(input("Enter the pixelation percentage (0-100): "))
        pixelated_image = pixelate(image, percent)

        # save pixelated image as new file
        pixelated_filename = "pixelated_" + filename
        pixelated_image.save(pixelated_filename)
        print("Pixelated image saved as", pixelated_filename)
except FileNotFoundError:
    print("Error: file not found")
