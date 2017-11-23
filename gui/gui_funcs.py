from gui.gui_vars import *


def link_btn_click(event):
    link_btn = event.widget
    btn_txt = link_btn["text"]
    if btn_txt == "连接":
        link_btn_var.set("断开")
        link_btn["bg"] = "#F94B4B"
        link_btn["activebackground"] = "#F94B4B"
    else:
        link_btn_var.set("连接")
        link_btn["bg"] = "#09F768"
        link_btn["activebackground"] = "#09F768"


def add_btn_click(event, lst_lb):
    lst_lb.insert("end", "default")
    lst_lb.select_clear(0, "end")
    lst_lb.select_set("end")


def del_btn_click(event, lst_lb):
    index_selected_tuple = lst_lb.curselection()
    if len(index_selected_tuple) > 0:
        lst_lb.delete(index_selected_tuple[0])
        lst_lb.select_set("end")


def lst_item_selected(event, det_input_widget_dist):
    lst_lb = event.widget
    item_text = lst_lb.get(0, "end")[lst_lb.curselection()[0]]
    print(item_text)
    name_widget = det_input_widget_dist["name"]
    name_widget.delete(1.0, "end")
    name_widget.insert("end", item_text)
