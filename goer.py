from PIL import Image, ImageDraw
import numpy as np
import io


def get_paste_region(i):
    return (i - 15, i, i + 160, i + 175)


def circular_image(img):
    height, width = img.size
    lum_img = Image.new('L', (height, width), 0)
    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(0, 0), (height, width)], 0, 360, fill=255, outline="white")
    img_arr = np.array(img)
    lum_img_arr = np.array(lum_img)
    final_img_arr = np.dstack((img_arr, lum_img_arr))
    new_img = Image.fromarray(final_img_arr)
    return new_img


def get_goed_image(img):
    # Read base image
    base = Image.open("base.png")

    # Read Profile Image
    profile = Image.open(io.BytesIO(img))
    profile = profile.resize((175, 175))
    # profile = circular_image(profile)

    # Paste profile on base
    paste_region = get_paste_region(275)
    base.paste(profile,  paste_region)
    output = io.BytesIO()
    base.save(output, format='PNG')
    base.save("output.png")
    return output.getvalue()
