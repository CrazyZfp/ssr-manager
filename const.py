# path of config.json
CONFIG_PATH = "./config.json"

# keys in config.json
KEY_SSR_PATH = "ssr_path"  # key to the path of shadowsocksr/shadowsocks/local.py
KEY_SSR_LIST = "ssr_list"  # key to the list of ssr settings

# name for default ssr
DEFAULT = "default"
# default ssr modle
DEFAULT_SSR = {
    "remarks": "default",
    "server": "192.168.1.1",
    "port": 0,
    "local": "127.0.0.1",
    "local_port": 8080,
    "password": "password",
    "obfs": "plain",
    "obfsparam": "",
    "method": "none",
    "protocol": "origin",
    "protoparam": "",
    "ssr_url": "ssr://MTkyLjE2OC4xLjE6MDpvcmlnaW46bm9uZTpwbGFpbjpjR0Z6YzNkdmNtUT0vP29iZnNwYXJhbT0mcHJvdG9wYXJhbT0mc3NybmFtZT1aR1ZtWVhWc2RBPT0="
}

# pairs of Lable widget text with Text widget key in det_frm
LAB_NAME_KEY = [("代理名称", "remarks"), ("*远程IP", "server"), ("*远程端口", "port"),
                ("本地IP", "local"), ("本地端口", "local_port"), ("*连接密码", "password"),
                ("*混淆方式", "obfs"), ("混淆参数", "obfsparam"), ("*加密方法", "method"),
                ("*协议", "protocol"), ("协议参数", "protoparam"), ("URL", "ssr_url")]

# ssr_path_verify RETURN VALUE
NO_CONFIG = 0  # no config.json
FAKE_SSR = 1  # ssr_path in config.json is invalid
SUCCESS = 2  # ssr_path in config.json is valid

# file operation mode
W = "w"
R = "r"

# link_btn text
CONNECT = "连接"
SHUTDOWN = "断开"

# link_btn color
CONNECT_COLOR = "#09F768"
SHUTDOWN_COLOR = "#F94B4B"

# 以下为下拉列表预设值
# 混淆方式 obfs
OBFS_LST = ("plain", "http_simple", "http_post", "tls_simple", "tls1.2_ticket_auth")
# 协议 protocol
PROTOCOL_LST = ("origin", "verify_simple", "verify_sha1", "auth_sha1", "auth_sha1_v2", "auth_sha1_v4",
                "auth_aes128_sha1", "auth_aes128_md5", "auth_chain_a", "auth_chain_b", "auth_chain_c", "auth_chain_d")
# 加密方法 method
METHOD_LST = ("none", "table", "rc4", "rc4-md5", "rc4-md5-6", "aes-128-cfb", "aes-192-cfb", "aes-256-cfb",
              "aes-128-ctr", "aes-192-ctr", "aes-256-ctr", "bf-cfb", "camellia-128-cfb",
              "camellia-192-cfb", "camellia-256-cfb", "salsa20", "chacha20", "chacha20-ietf")
