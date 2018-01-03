import json
import os
from os.path import isfile
import re
import gui.global_vars as gvars
from const import CONFIG_PATH, KEY_SSR_PATH, SUCCESS, FAKE_SSR, W, R


def get_ssr_dir():
    ssr_path = get_ssr_path_from_config()
    if ssr_path is None:
        return '~'
    else:
        return re.sub("^/[^/]+\.py$", '', ssr_path)


def get_ssr_path_from_config():
    """从配置文件(全局变量)中读取SSR路径"""
    if KEY_SSR_PATH in gvars.ssr_config:
        return gvars.ssr_config[KEY_SSR_PATH]
    else:
        return None


def set_ssr_path(ssr_path):
    """设置SSR文件的路径"""
    gvars.ssr_config[KEY_SSR_PATH] = ssr_path
    update_config(gvars.ssr_config)


def read_config():
    """读取本程序的配置文件(包括SSR服务器配置)"""
    config_exists = isfile(CONFIG_PATH)
    if not config_exists:
        os.mknod(CONFIG_PATH)
    else:
        with open(CONFIG_PATH, R) as f:
            ssr_config = json.load(f)
            gvars.ssr_config = ssr_config


def ssr_path_verify(ssr_path=None):
    """校验ssr_path指向的文件存在，若未给定参数，则校验配置文件中设置的ssr_path存在"""
    if ssr_path is None:
        ssr_path = get_ssr_path_from_config()
        if ssr_path is None:
            return FAKE_SSR
    if isfile(ssr_path):
        return SUCCESS

    return FAKE_SSR


def update_config(config_dict):
    """更新本程序的配置文件"""
    with open(CONFIG_PATH, W) as f:
        json.dump(config_dict, f, indent=4, sort_keys=True)
