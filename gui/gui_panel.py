from tkinter import *

from gui.gui_config import *


class App:
    det_input_widget_dist = {}

    def init(self):
        window = Tk()

        window.title("ssr-manager")
        # window.geometry("900x400")
        window.geometry("550x350")
        window.resizable(width=False, height=False)

        win_frm = Frame(window)
        win_frm.pack(side="top", pady=10)

        self.det_frm_widget = self.det_init(win_frm)
        self.lst_frm_widget = self.lst_init(win_frm)
        # qr_init(win_frm)

        return window

    # 列表部分 初始化
    def lst_init(self, win_frm):
        from gui.gui_vars import lst_listvar
        from gui.gui_funcs import add_btn_click, del_btn_click, lst_item_selected

        lst_frm = Frame(win_frm, frm_cnf)
        lst_frm.grid(frm_grid_cnf, column=0)

        lb = Listbox(lst_frm, lst_lb_cnf, listvariable=lst_listvar)
        lb.bind("<<ListboxSelect>>", lambda event: lst_item_selected(event, self.det_input_widget_dist))
        lb.grid(row=0, column=0, columnspan=2)

        add_btn = Button(lst_frm, text="新增")
        del_btn = Button(lst_frm, text="删除")

        add_btn.bind("<Button-1>", lambda event: add_btn_click(event, lb))
        del_btn.bind("<Button-1>", lambda event: del_btn_click(event, lb))

        add_btn.grid(row=1, column=0)
        del_btn.grid(row=1, column=1)

        return lst_frm

    # 详情部分 初始化
    def det_init(self, win_frm):
        from gui.gui_vars import link_btn_var
        from gui.gui_funcs import link_btn_click

        det_frm = Frame(win_frm, frm_cnf)
        det_frm.grid(frm_grid_cnf, column=1)

        lab_name_key = [("代理名称", "name"), ("*远程IP", "server"), ("*远程端口", "server_port"),
                        ("本地IP", "local"), ("本地端口", "local_port"), ("*连接密码", "password"),
                        ("*混淆方式", "obfs"), ("混淆参数", "obfs_param"), ("*加密方法", "method"),
                        ("*协议", "protocol"), ("协议参数", "protocol_param")]

        for index, (lab_name, input_key) in enumerate(lab_name_key):
            lb = Label(det_frm, det_label_cnf, text=lab_name)
            tx = Text(det_frm, det_text_cnf)
            self.det_input_widget_dist[input_key] = tx

            lb.grid(column=0, row=index)
            tx.grid(column=1, row=index)

        det_btn_frm = Frame(det_frm, frm_cnf, relief=FLAT)
        det_btn_frm.grid(row=len(lab_name_key), column=0, columnspan=2)

        save_btn = Button(det_btn_frm, text="保存")
        link_btn = Button(det_btn_frm, textvariable=link_btn_var, bg="#09F768", activebackground="#09F768")

        save_btn.grid(row=len(lab_name_key), column=0, padx=20)
        link_btn.grid(row=len(lab_name_key), column=1, padx=20)

        link_btn.bind("<Button-1>", link_btn_click)

        return det_frm

        # 二维码部分 初始化
        # def qr_init(win_frm):
        #     qr_frm = Frame(win_frm, cnf_frm, bg="green", width=280)
        #     qr_frm.grid(cnf_frm_grid, column=2)
