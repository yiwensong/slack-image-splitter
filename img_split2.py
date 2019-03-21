import numpy as np
from PIL import Image

IMAGE = '/Users/yiws/Desktop/Screen Shot 2018-09-20 at 12.00.46 PM.png'
im = Image.open(IMAGE)
rgba_im = im.convert('RGBA')
data = np.array(rgba_im)
for row in data:
    for pixels in row:
        if all(pixels == 255):
            pixels[0] = 0
            pixels[1] = 0
            pixels[2] = 0
            pixels[3] = 0

new_im = Image.fromarray(data)
with open('/Users/yiws/Downloads/new_ss.png', 'wb') as f:
    new_im.save(f)


crop1 = new_im.crop((0,0,44,44))
crop2 = new_im.crop((44,0,88,44))
crop3 = new_im.crop((88,0,132,44))

with open('/Users/yiws/Downloads/channel1.png', 'wb') as f:
    crop1.save(f)
with open('/Users/yiws/Downloads/channel2.png', 'wb') as f:
    crop2.save(f)
with open('/Users/yiws/Downloads/channel3.png', 'wb') as f:
    crop3.save(f)
