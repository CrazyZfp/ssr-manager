from pyzbar.pyzbar import decode
import qrcode
from PIL import Image
from ssr_url_util import decode_ssr, encode_ssr


def decode_qr(img_path):
    qr_decode_obj_list = decode(Image.open(img_path))
    ssr_lst = []
    for qr_decode_obj in qr_decode_obj_list:
        ssr_url = qr_decode_obj.data.decode()
        ssr = decode_ssr(ssr_url)
        ssr["ssr_url"] = ssr_url
        ssr_lst.append(ssr)
    print(ssr_lst)
    return ssr_lst


def encode_qr(ssr):
    ssr_url = encode_ssr(ssr)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(ssr_url)
    qr.make(fit=True)
    img = qr.make_image()
    # img.show()


decode_qr("tt.png")
