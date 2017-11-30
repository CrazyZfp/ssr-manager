# path of config.json
CONFIG_PATH = "./config.json"

# keys in config.json
KEY_SSR_PATH = "ssr_path"  # key to the path of shadowsocksr/shadowsocks/local.py
KEY_SSR_LIST = "ssr_list"  # key to the list of ssr settings

# name for default ssr
DEFAULT = "default"
# default ssr modle
DEFAULT_SSR = {
    "ssr_name": "default",
    "server": "",
    "server_port": 0,
    "local": "127.0.0.1",
    "local_port": 8080,
    "password": "",
    "obfs": "",
    "obfs_param": "",
    "method": "",
    "protocol": "",
    "protocol_param": ""
}

# pairs of Lable widget text with Text widget key in det_frm
LAB_NAME_KEY = [("代理名称", "ssr_name"), ("*远程IP", "server"), ("*远程端口", "server_port"),
                ("本地IP", "local"), ("本地端口", "local_port"), ("*连接密码", "password"),
                ("*混淆方式", "obfs"), ("混淆参数", "obfs_param"), ("*加密方法", "method"),
                ("*协议", "protocol"), ("协议参数", "protocol_param")]

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
