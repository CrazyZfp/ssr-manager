import json
import os
from os.path import isfile

import gui.global_vars as gvars
from const import CONFIG_PATH, NO_CONFIG, KEY_SSR_PATH, SUCCESS, FAKE_SSR, W, R


def ssr_path_verify():
    config_exists = isfile(CONFIG_PATH)
    if not config_exists:
        os.mknod(CONFIG_PATH)
        return NO_CONFIG
    else:
        with open(CONFIG_PATH, R) as f:
            ssr_config = json.load(f)
            gvars.ssr_config = ssr_config

        if KEY_SSR_PATH in ssr_config:
            ssr_path = ssr_config[KEY_SSR_PATH]
            if isfile(ssr_path):
                return SUCCESS

    return FAKE_SSR


def update_config(config_dict):
    with open(CONFIG_PATH, W) as f:
        json.dump(config_dict, f, indent=4, sort_keys=True)
