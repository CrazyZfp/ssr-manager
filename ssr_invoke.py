from subprocess import check_output
import sys

LONG_SHORT_OPTS_MAP = {
    "server_port": "-p",
    "password": "-k",
    "local_port": "-l",
    "server:": "-s",
    "method": "-m",
    "protocol": "-O",
    "obfs": "-o",
    "protocol_param": "-G",
    "obfs_param": "-g",
    "local_address": "-b"
}


def link_ssr(ssr_path, ssr_info):
    try:
        cmd = "python3 {} {}".format(ssr_path, ' '.join(gen_opt_list(ssr_info)))
        print(cmd)
        re = check_output(cmd, shell=True)
        # re = check_output("sleep 2;echo aaa", shell=True)
        print(re)
    except Exception as e:
        print("error occured when try to link ssr: ", str(e), file=sys.stderr)


def gen_opt_list(ssr_info):
    opt_list = []
    for (k, v) in ssr_info.items():
        if k in LONG_SHORT_OPTS_MAP:
            opt_list.append(LONG_SHORT_OPTS_MAP[k])
            opt_list.append(v)

    return opt_list
