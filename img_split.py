import numpy as np
import png


FILE = '/Users/yiws/Desktop/Screen Shot 2018-09-20 at 12.00.46 PM.png'

img = png.Reader(FILE).read()
img_data = img[2]

out1 = []
out2 = []
out3 = []
for row in img_data:
    row = list(row)
    out1.append(row[:img[1]*4])
    out2.append(row[img[1]*3:2*img[1]*4])
    out3.append(row[2*img[1]*4:])

    print (out1)
    print (out2)
    print (out3)

with open('/Users/yiws/Downloads/channel1.png', 'wb') as f:
    w = png.Writer(img[1], img[1])
    w.write(f, out1)
with open('/Users/yiws/Downloads/channel2.png', 'wb') as f:
    w = png.Writer(img[1], img[1])
    w.write(f, out2)
with open('/Users/yiws/Downloads/channel3.png', 'wb') as f:
    w = png.Writer(img[1], img[1])
    w.write(f, out3)
