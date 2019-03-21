import numpy as np
from PIL import Image

IMAGE = '/Users/yiws/Desktop/Screen Shot 2019-03-21 at 10.57.43 AM.png'
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
with open('/Users/yiws/Downloads/subscribe.png', 'wb') as f:
    new_im.save(f)

x_dim, y_dim = new_im.size

max_dim = min(128, x_dim, y_dim)

x_needed = (x_dim - 1)//max_dim + 1
y_needed = (y_dim - 1)//max_dim + 1

for x in range(x_needed):
    for y in range(y_needed):
        left = x * max_dim
        right = (x + 1) * max_dim
        top = y * max_dim
        bottom = (y + 1) * max_dim
        crop = new_im.crop((left, top, right, bottom))

        fname = f'/Users/yiws/Downloads/subscribe-{x}-{y}.png'
        with open(fname, 'wb') as f:
            crop.save(f)
