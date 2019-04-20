import subprocess
import sys
from log.logger import get_logger

logger = get_logger("ssr_invoke")

LONG_SHORT_OPTS_MAP = {
    "port": "-p",
    "password": "-k",
    "local_port": "-l",
    "server": "-s",
    "method": "-m",
    "protocol": "-O",
    "obfs": "-o",
    "protoparam": "-G",
    "obfsparam": "-g",
    "local_address": "-b"
}

ssr_process = None


def link_ssr(ssr_path, ssr_info):
    try:
        cmd = ['python3', ssr_path] + gen_opt_list(ssr_info)
        # re = check_output(cmd, shell=True)
        global ssr_process
        ssr_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        # print(process.wait())
        logger.debug("Start SSR Process with cmd: {}".format(cmd))
        print(ssr_process.stderr.readline())
        print(ssr_process.stderr.readline())
        print(ssr_process.stderr.readline())
        # ssr_process.stderr
        # print(ssr_process.stderr.readline())
        # print(process.pid)
    except Exception as e:
        print("error occurred when try to link ssr: ", str(e), file=sys.stderr)


def terminate_process():
    global ssr_process
    if ssr_process:
        ssr_process.terminate()
        logger.info("SSR Process terminated!")


def gen_opt_list(ssr_info):
    opt_list = []
    for (k, v) in ssr_info.items():
        if k in LONG_SHORT_OPTS_MAP:
            opt_list.append(LONG_SHORT_OPTS_MAP[k])
            if not type(v) is str:
                opt_list.append(str(v))
            else:
                opt_list.append(v)

    return opt_list
