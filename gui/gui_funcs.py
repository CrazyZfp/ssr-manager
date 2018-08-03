from gui.global_vars import ssr_config, det_input_widget_dict
from gui.tk_vars import *
from tkinter.constants import *
from multiprocessing import Process
import copy

from const import *
from config_operator import update_config, ssr_path_verify
from log.logger import getLogger
from ssr_invoke import link_ssr
from ssr_url_util import encode_ssr
from qr_util import encode_qr

logger = getLogger("gui_funcs")

ssr_selected_index = 0

p = None


def init_panel_data():
    if KEY_SSR_LIST in ssr_config:
        ssr_list = ssr_config[KEY_SSR_LIST]
        if len(ssr_list) > 0:
            remarks_list = [ssr["remarks"] for ssr in ssr_list]
            lst_listvar.set(remarks_list)
            # det_input_widget_dict["lst_lb"].selection_set(0)
            render_det_data()
            return


def add_default_ssr():
    if KEY_SSR_LIST in ssr_config:
        ssr_config[KEY_SSR_LIST].append(copy.deepcopy(DEFAULT_SSR))
        logger.debug(str(DEFAULT_SSR))
        logger.debug(str(ssr_config))
    else:
        ssr_config[KEY_SSR_LIST] = [copy.deepcopy(DEFAULT_SSR)]
    update_config(ssr_config)


def update_ssr(index):
    ssr = ssr_config[KEY_SSR_LIST][index]
    for (name, key) in LAB_NAME_KEY:
        text_widget = det_input_widget_dict[key]
        ssr[key] = text_widget.get().strip()

    del ssr["ssr_url"]
    ssr_url = encode_ssr(ssr)
    print("update_ssr - ssr_url: {}".format(ssr_url))
    ssr["ssr_url"] = ssr_url

    init_panel_data()
    update_config(ssr_config)


def del_ssr(index):
    del ssr_config[KEY_SSR_LIST][index]
    update_config(ssr_config)


def link_btn_click_handler(event):
    """
    "连接/断开"按钮 点击事件
    """
    link_btn = event.widget
    btn_txt = link_btn["text"]
    global p
    if btn_txt == CONNECT:
        if ssr_path_verify() == FAKE_SSR:
            from gui.gui_panel import fake_ssr_path_warning
            fake_ssr_path_warning()
            return
        link_btn_var.set(SHUTDOWN)
        link_btn["bg"] = SHUTDOWN_COLOR
        link_btn["activebackground"] = SHUTDOWN_COLOR
        p = Process(target=link_ssr,
                    args=(ssr_config[KEY_SSR_PATH], ssr_config[KEY_SSR_LIST][ssr_selected_index]))
        p.start()
    else:
        if p is not None:
            p.terminate()
        link_btn_var.set(CONNECT)
        link_btn["bg"] = CONNECT_COLOR
        link_btn["activebackground"] = CONNECT_COLOR


def add_btn_click_handler(_):
    """
    "新增"按钮 点击事件
    """
    lst_lb = det_input_widget_dict["lst_lb"]
    lst_lb.insert(END, DEFAULT)
    add_default_ssr()
    lst_lb.select_clear(0, END)
    lst_lb.select_set(END)
    render_det_data()


def save_btn_click_handler(_):
    """
    "保存"按钮 点击事件
    """
    lst_lb = det_input_widget_dict["lst_lb"]
    if lst_lb.size() == 0:
        add_default_ssr()
    update_ssr(ssr_selected_index)


def del_btn_click_handler(_):
    """
    "删除"按钮 点击事件
    """
    lst_lb = det_input_widget_dict["lst_lb"]
    index_selected_tuple = lst_lb.curselection()
    if len(index_selected_tuple) > 0:
        selected_index = index_selected_tuple[0]
        lst_lb.delete(selected_index)
        del_ssr(selected_index)

        lst_lb_size = lst_lb.size()
        if lst_lb_size > selected_index:
            lst_lb.select_set(selected_index)
            render_det_data()
        elif lst_lb_size == selected_index:
            lst_lb.select_set(END)
            render_det_data()
            # else:
            #     add_btn_click_handler(_)

def encode_ssr_to_qr():
    print("lalalal")
    global ssr_selected_index
    ssr = ssr_config[KEY_SSR_LIST][ssr_selected_index]
    encode_qr(ssr)


def lst_item_selected_handler(e):
    # e.x_root == e.y_root == -1 表示list中有item被点击(foucs)
    # e.x_root == e.y_root == 0 表示list中item焦点丢失(loose foucs)
    # loose foucs 的事件不需要重新渲染
    if e.x_root == -1:
        global ssr_selected_index
        lst_lb = det_input_widget_dict["lst_lb"]
        # 当前选择的item与上一次选择的item是同一个item时,不进行渲染
        if ssr_selected_index != lst_lb.curselection()[0]:
            render_det_data()


def render_det_data():
    global ssr_selected_index

    lst_lb = det_input_widget_dict["lst_lb"]
    if lst_lb.curselection():
        ssr_selected_index = lst_lb.curselection()[0]

    # prevent exception when lst_lb lose focus
    if lst_lb.size() != 0:
        ssr = ssr_config[KEY_SSR_LIST][ssr_selected_index]
        print("render_det_data - ssr_url: {}".format(ssr['ssr_url']))
        for (name, key) in LAB_NAME_KEY:
            if key == "ssr_url":
                url_var.set(ssr[key])
            elif key in ["obfs", "method", "protocol"]:
                render_data_if_combobox(key, ssr[key])
            else:
                det_input_widget = det_input_widget_dict[key]
                det_input_widget.delete(0, END)
                det_input_widget.insert(END, ssr[key])
    # clear det_input_widgets when no item in lst_lb left
    elif lst_lb.size() == 0:
        for (name, key) in LAB_NAME_KEY:
            if not render_data_if_combobox(key, ""):
                det_input_widget_dict[key].delete(0, END)


def render_data_if_combobox(key, value):
    try:
        if key == "obfs":
            idx = OBFS_LST.index(value)
        elif key == "method":
            idx = METHOD_LST.index(value)
        elif key == "protocol":
            idx = PROTOCOL_LST.index(value)
        else:
            return False
    except ValueError:
        idx = 0
    det_input_widget_dict[key].current(idx)
    return True
