# import qrcode
# import zbarlight
# from PIL import Image
#
# file_path = 'qr.png'
#
# opts_key_len_list = [('obfsparam=', 10), ('remark=', 7)]
#
# with open(file_path, 'rb') as image_file:
#     image = Image.open(image_file)
#     image.load()
# codes_url = zbarlight.scan_codes('qrcode', image)
# code = bytes.decode(codes_url[0]).lstrip("ssr://").replace("_", "/")
# print(code)

from pyscreenshot import grab
# import pyautogui

im = grab()
im.show()