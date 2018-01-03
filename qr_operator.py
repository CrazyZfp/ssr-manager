# from PIL import Image
# import zbarlight
# import gi
#
# from tkinter.filedialog import askopenfilename
#
# pp = askopenfilename(title='aa', filetypes=[("python files", "*.py")], initialdir='~')
#
# print(pp)

import re

a = re.sub("/[^/]+\.py$", '', "http://asdfasfd/asdf/dsf/sdf.py")
print(a)
