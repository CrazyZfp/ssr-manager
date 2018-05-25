from pyzbar.pyzbar import decode
import qrcode
from PIL import Image
from ssr_url_util import decode_ssr, encode_ssr


def decode_qr(img_path):
    ssr_url_bytes_lst = decode(Image.open('tt.png'))
    ssr_lst = []
    for ssr_url_bytes in ssr_url_bytes_lst:
        ssr = decode_ssr(ssr_url_bytes.decode("utf-8"))
        ssr["ssr_url"] = ssr_url_bytes
        ssr_lst.append(ssr)
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
    img.show()


encode_qr({
    "local": "127.0.0.1",
    "local_port": "8080",
    "method": "rc4-md5-6",
    "obfs": "http_simple",
    "obfsparam": "",
    "password": "password",
    "port": "0",
    "protocol": "auth_aes128_sha1",
    "protoparam": "",
    "server": "192.168.1.1",
    "remarks": "default"
})

decode_qr("test.png")
