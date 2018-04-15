from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showwarning
from const import LAB_NAME_KEY, CONNECT_COLOR
from gui.gui_config import *


def fake_ssr_path_warning():
    showwarning("SSR未设置", "请先通过 顶部菜单栏->设置->SSR路径 设置正确的SSR路径")


class App:
    def __init__(self):
        self.window = Tk()

        self.window.title("ssr-manager")
        # window.geometry("900x400")
        self.window.geometry("550x350")
        self.window.resizable(width=False, height=False)

        self.win_frm = Frame(self.window)
        self.win_frm.pack(side="top", pady=10)

        self.det_frm_widget = self.det_init()
        self.lst_frm_widget = self.lst_init()
        self.menu_init()

        from gui.gui_funcs import init_panel_data
        init_panel_data()

    def lst_init(self):
        """列表部分 初始化"""
        from gui.global_vars import det_input_widget_dict
        from gui.tk_vars import lst_listvar
        from gui.gui_funcs import add_btn_click_handler, del_btn_click_handler, lst_item_selected_handler

        lst_frm = Frame(self.win_frm, frm_cnf)
        lst_frm.grid(frm_grid_cnf, column=0)

        scrollbar = Scrollbar(lst_frm, orient=VERTICAL)
        scrollbar.grid(column=2, sticky=N + S)

        lb = Listbox(lst_frm, lst_lb_cnf, listvariable=lst_listvar, yscrollcommand=scrollbar.set)
        lb.bind("<<ListboxSelect>>", lst_item_selected_handler)
        lb.grid(row=0, column=0, columnspan=2)
        det_input_widget_dict["lst_lb"] = lb

        scrollbar.config(command=lb.yview)

        add_btn = Button(lst_frm, text="新增")
        del_btn = Button(lst_frm, text="删除")

        add_btn.bind("<Button-1>", add_btn_click_handler)
        del_btn.bind("<Button-1>", del_btn_click_handler)

        add_btn.grid(row=1, column=0)
        del_btn.grid(row=1, column=1)

        return lst_frm

    def det_init(self):
        """详情部分 初始化"""
        from gui.global_vars import det_input_widget_dict
        from gui.tk_vars import link_btn_var
        from gui.gui_funcs import link_btn_click_handler, save_btn_click_handler

        det_frm = Frame(self.win_frm, frm_cnf)
        det_frm.grid(frm_grid_cnf, column=1)

        for index, (lab_name, input_key) in enumerate(LAB_NAME_KEY):
            lb = Label(det_frm, det_label_cnf, text=lab_name)
            tx = Text(det_frm, det_text_cnf)
            det_input_widget_dict[input_key] = tx

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

    def menu_init(self):
        """菜单栏 初始化"""
        menu_bar = Menu(self.window)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="二维码导入")
        file_menu.add_command(label="二维码导出")
        menu_bar.add_cascade(label="文件", menu=file_menu)

        config_menu = Menu(menu_bar, tearoff=0)
        config_menu.add_command(label="SSR路径", command=self.file_dialog_open)
        menu_bar.add_cascade(label="设置", menu=config_menu)

        menu_bar.add_command(label="帮助")

        self.window.config(menu=menu_bar)

    def file_dialog_open(self):
        """开启文件窗口"""
        from config_operator import set_ssr_path, get_ssr_dir
        ssr_path = askopenfilename(title="设置SSR路径", filetypes=[("python files", "*.py")],
                                   initialdir=get_ssr_dir(), parent=self.window)
        if ssr_path is not None and type(ssr_path) is str:
            set_ssr_path(ssr_path)

    def start(self):
        self.window.mainloop()
