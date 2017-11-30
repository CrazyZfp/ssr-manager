from gui.global_vars import ssr_config, det_input_widget_dist
from gui.tk_vars import *
from tkinter.constants import *
from const import CONNECT, SHUTDOWN, CONNECT_COLOR, SHUTDOWN_COLOR, KEY_SSR_LIST, DEFAULT_SSR, LAB_NAME_KEY, DEFAULT
from config_operator import update_config
from log.logger import getLogger
import copy

logger = getLogger("gui_funcs")

ssr_selected_index = -1


def init_panel_data():
    if KEY_SSR_LIST in ssr_config:
        ssr_list = ssr_config[KEY_SSR_LIST]
        if len(ssr_list) > 0:
            ssr_name_list = [ssr["ssr_name"] for ssr in ssr_list]
            lst_listvar.set(ssr_name_list)
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
        text_widget = det_input_widget_dist[key]
        ssr[key] = text_widget.get("1.0", END).strip()
    init_panel_data()
    update_config(ssr_config)


def del_ssr(index):
    del ssr_config[KEY_SSR_LIST][index]
    update_config(ssr_config)


def link_btn_click_handler(event):
    link_btn = event.widget
    btn_txt = link_btn["text"]
    if btn_txt == CONNECT:
        link_btn_var.set(SHUTDOWN)
        link_btn["bg"] = SHUTDOWN_COLOR
        link_btn["activebackground"] = SHUTDOWN_COLOR
    else:
        link_btn_var.set(CONNECT)
        link_btn["bg"] = CONNECT_COLOR
        link_btn["activebackground"] = CONNECT_COLOR


def add_btn_click_handler(_):
    lst_lb = det_input_widget_dist["lst_lb"]
    lst_lb.insert(END, DEFAULT)
    add_default_ssr()
    lst_lb.select_clear(0, END)
    lst_lb.select_set(END)
    render_det_data()


def save_btn_click_handler(_):
    lst_lb = det_input_widget_dist["lst_lb"]
    if lst_lb.size() == 0:
        add_default_ssr()
    update_ssr(ssr_selected_index)


def del_btn_click_handler(_):
    lst_lb = det_input_widget_dist["lst_lb"]
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


def lst_item_selected_handler(_):
    render_det_data()


def render_det_data():
    lst_lb = det_input_widget_dist["lst_lb"]
    item_selected_list = lst_lb.curselection()
    # prevent exception when lst_lb lose focus
    if len(item_selected_list) == 1:
        global ssr_selected_index
        ssr_selected_index = item_selected_list[0]
        ssr = ssr_config[KEY_SSR_LIST][ssr_selected_index]
        for (name, key) in LAB_NAME_KEY:
            det_input_widget = det_input_widget_dist[key]
            det_input_widget.delete(1.0, END)
            det_input_widget.insert(END, ssr[key])
    # clear det_input_widgets when no item in lst_lb left
    elif lst_lb.size() == 0:
        for (name, key) in LAB_NAME_KEY:
            det_input_widget_dist[key].delete(1.0, END)
