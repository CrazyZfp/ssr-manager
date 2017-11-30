# coding=utf-8
import logging.config
import os

logging.config.fileConfig(os.getcwd() + "/log/logger.conf")


def getLogger(module_name):
    return logging.getLogger("{}".format(module_name))
