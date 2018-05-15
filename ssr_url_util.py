import base64


def b64_encode(content_str, altchars=b'-_'):
    return bytes.decode(base64.b64encode(bytes(content_str), altchars))


def b64_decode(content_b64):
    return bytes.decode(base64.b64decode(content_b64), "utf-8")


def uri_to_map(uri_str):
    uri_params = uri_str.split("&")
    return dict(param.split("=") for param in uri_params)


def encode_ssr(ssr):
    obfp_base64 = b64_encode(ssr['obfs_param'])
    ptcp_base64 = b64_encode(ssr['protocol_param'])
    name_base64 = b64_encode(ssr['ssr_name'])
    locp_base64 = b64_encode(ssr['local_port'])
    loc_base64 = b64_encode(ssr['local'])

    password_base64 = b64_encode(ssr['password'])
    param_base64 = "obfsparam={}&protoparam={}&ssrname={}&localport={}&local={}".format(obfp_base64, ptcp_base64,
                                                                                        name_base64, locp_base64,
                                                                                        loc_base64)
    pwd_param = b64_encode("{}/?{}".format(password_base64, param_base64))

    return "ssr://" + b64_encode("{server}:{port}:{protocol}:{method}:{obfs}:{pwd_param}"
                                 .format(server=ssr["server"], port=ssr["port"],
                                         protocol=ssr["protocol"], method=ssr["method"],
                                         obfs=ssr["obfs"], pwd_param=pwd_param))


def decode_ssr(ssr_url_b64):
    ssr = {}

    ssr_url = b64_decode(ssr_url_b64.lstrip("ssr://").replace("_", "/").replace("-", "+"))
    ssr_arr = ssr_url.split(":")

    ssr['server'] = ssr_arr[0]
    ssr['port'] = int(ssr_arr[1])
    ssr['protocol'] = ssr_arr[2]
    ssr['method'] = ssr_arr[3]
    ssr['obfs'] = ssr_arr[4]

    pwd_b64, param_b64_str = ssr_arr[5].split("/?")
    ssr["password"] = b64_decode(pwd_b64)

    param_map_b64 = uri_to_map(param_b64_str)
    for k, v in param_map_b64.items():
        ssr[k] = b64_decode(v)

    return ssr
