# QRcode generation
# Haijiang 2022-7-20

import pyqrcode
import png

def generate(link, name, scale):
    qr_code = pyqrcode.create(link)
    qr_code.png(name, scale=scale)

# generate('https://cn.ntcdoon.org/714160-how-to-install-the-png-PXMXLK', 'test.png', 5)


# import QRcode as qr
# qr.generate('https://cn.ntcdoon.org/714160-how-to-install-the-png-PXMXLK', 'test.png', 5)