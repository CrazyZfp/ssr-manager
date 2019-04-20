# coding=utf-8
import logging.config
import os

logging.config.fileConfig(os.getcwd() + "/log/logger.conf")


def get_logger(module_name):
    return logging.getLogger("{}".format(module_name))
