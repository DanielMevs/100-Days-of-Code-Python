from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='./images', title='Select an Image:')


# print(filename)


def add_watermark(image, wm_text):
    # Creates the Image object
    opened_image = Image.open(image)

    # Get Image size
    image_width, image_height = opened_image.size

    # Draw on Image
    draw = ImageDraw.Draw(opened_image)

    # For Windows, change font type to 'arial'
    font = ImageFont.truetype('arial.ttf', 36)

    textwidth, textheight = draw.textsize(wm_text, font)

    # Calculate the x,y coordinates of the text
    margin = 10
    x = image_width - textwidth - margin
    y = image_height - textheight - margin

    # Add the watermark
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    # Show the new image
    opened_image.show()

    # Save the new image
    # opened_image.save()


add_watermark(filename, 'Testing')