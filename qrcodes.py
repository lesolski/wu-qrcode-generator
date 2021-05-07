import qrcode
from PIL import Image
import argparse
import os
import numpy as np

# ARGPARSER
parser = argparse.ArgumentParser(description='Make a custom WU QR code.')
parser.add_argument('text', help='Text that you want to put into qr code.', type=str)
parser.add_argument('--color', help='HEX color for logo and qr code, default is black', type=str, default='#000000')
parser.add_argument('--path', help='Path and name of file where to save it', default=os.getcwd() + '/qrcode.png', type=str)
parser.add_argument('--size', help='Tuple of width and hight 200x200 is default, first add width then hight', type=str, default=('100x100'))
args = parser.parse_args()


def make_qr_code(text:str, color:str, path:str, resize_tuple:str):
    """Makes QR Code with embedded WU logo init"""

    qr = qrcode.QRCode(
        version=8,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )

    qr.add_data(text)
    qr.make(fit=True)

    # qrcode as background
    bg = qr.make_image(fill_color=color, back_color='white')
    bg_w, bg_h = bg.size

    # logo as foreground
    logo = Image.open('logo/wu-logo.png', 'r')
    data = np.array(logo)

    # changing color of logo to desired color
    r1, g1, b1 = 255, 255, 255
    r2, g2, b2 = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) # convert hex to rgb

    # reading colors
    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]

    mask = (red < r1) & (green < g1) & (blue < b1) # mask for fill
    data[:,:,:3][mask] = [r2, g2, b2] # converting colors

    logo = Image.fromarray(data)
    logo_w, logo_h = logo.size

    # putting logo over qr code
    offset = ((bg_w - logo_w) // 2, (bg_h - logo_h) // 2)
    bg.paste(logo, offset, logo)

    x, y = resize_tuple.split('x')
    qr_code = bg.resize((int(x), int(y)))
    qr_code.save(path, format='PNG')

    return

make_qr_code(text=args.text, color=args.color, path=args.path, resize_tuple=args.size)
