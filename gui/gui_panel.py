from tkinter import *
from const import LAB_NAME_KEY, CONNECT_COLOR
from gui.gui_config import *


class App:
    def __init__(self):
        window = Tk()

        window.title("ssr-manager")
        # window.geometry("900x400")
        window.geometry("550x350")
        window.resizable(width=False, height=False)

        win_frm = Frame(window)
        win_frm.pack(side="top", pady=10)

        self.det_frm_widget = self.det_init(win_frm)
        self.lst_frm_widget = self.lst_init(win_frm)
        self.window = window

        from gui.gui_funcs import init_panel_data
        init_panel_data()
        # qr_init(win_frm)

    # 列表部分 初始化
    def lst_init(self, win_frm):
        from gui.global_vars import det_input_widget_dist
        from gui.tk_vars import lst_listvar
        from gui.gui_funcs import add_btn_click_handler, del_btn_click_handler, lst_item_selected_handler

        lst_frm = Frame(win_frm, frm_cnf)
        lst_frm.grid(frm_grid_cnf, column=0)

        lb = Listbox(lst_frm, lst_lb_cnf, listvariable=lst_listvar)
        lb.bind("<<ListboxSelect>>", lst_item_selected_handler)
        lb.grid(row=0, column=0, columnspan=2)
        det_input_widget_dist["lst_lb"] = lb

        add_btn = Button(lst_frm, text="新增")
        del_btn = Button(lst_frm, text="删除")

        add_btn.bind("<Button-1>", add_btn_click_handler)
        del_btn.bind("<Button-1>", del_btn_click_handler)

        add_btn.grid(row=1, column=0)
        del_btn.grid(row=1, column=1)

        return lst_frm

    # 详情部分 初始化
    def det_init(self, win_frm):
        from gui.global_vars import det_input_widget_dist
        from gui.tk_vars import link_btn_var
        from gui.gui_funcs import link_btn_click_handler, save_btn_click_handler

        det_frm = Frame(win_frm, frm_cnf)
        det_frm.grid(frm_grid_cnf, column=1)

        for index, (lab_name, input_key) in enumerate(LAB_NAME_KEY):
            lb = Label(det_frm, det_label_cnf, text=lab_name)
            tx = Text(det_frm, det_text_cnf)
            det_input_widget_dist[input_key] = tx

            lb.grid(column=0, row=index)
            tx.grid(column=1, row=index)

        det_btn_frm = Frame(det_frm, frm_cnf, relief=FLAT)
        det_btn_frm.grid(row=len(LAB_NAME_KEY), column=0, columnspan=2)

        save_btn = Button(det_btn_frm, text="保存")
        link_btn = Button(det_btn_frm, textvariable=link_btn_var, bg=CONNECT_COLOR, activebackground=CONNECT_COLOR)

        save_btn.grid(row=len(LAB_NAME_KEY), column=0, padx=20)
        link_btn.grid(row=len(LAB_NAME_KEY), column=1, padx=20)

        link_btn.bind("<Button-1>", link_btn_click_handler)
        save_btn.bind("<Button-1>", save_btn_click_handler)

        return det_frm

        # 二维码部分 初始化
        # def qr_init(win_frm):
        #     qr_frm = Frame(win_frm, cnf_frm, bg="green", width=280)
        #     qr_frm.grid(cnf_frm_grid, column=2)
