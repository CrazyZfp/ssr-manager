from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showwarning
from const import LAB_NAME_KEY, CONNECT_COLOR, OBFS_LST, PROTOCOL_LST, METHOD_LST
from gui.gui_config import *


def fake_ssr_path_warning():
    showwarning("SSR未设置", "请先通过 顶部菜单栏->设置->SSR路径 设置正确的SSR路径")


def is_int(k):
    if k == "":
        return True
    try:
        int(k)
        return True
    except ValueError:
        return False


class App:
    def __init__(self):
        self.window = Tk()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.title("ssr-manager")
        self.window.geometry("550x380")
        self.window.resizable(width=False, height=False)

        self.win_frm = Frame(self.window)
        self.win_frm.pack(side="top", pady=10)

        self.det_init()
        self.lst_frm_widget = self.lst_init()
        self.menu_init()

        from gui.gui_funcs import init_panel_data
        init_panel_data()

    def on_closing(self):
        from tkinter import messagebox
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            from ssr_invoke import terminate_process
            terminate_process()
            self.window.destroy()

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
        from gui.tk_vars import link_btn_var, url_var
        from gui.gui_funcs import link_btn_click_handler, save_btn_click_handler
        from tkinter.ttk import Combobox

        det_frm = Frame(self.win_frm, frm_cnf)
        self.det_frm_widget = det_frm
        det_frm.grid(frm_grid_cnf, column=1)
        # 注册整型检验方法，用于Entry的validatecommand属性
        is_int_valid_cmd = det_frm.register(is_int)

        for index, (lab_name, input_key) in enumerate(LAB_NAME_KEY):
            lb = Label(det_frm, det_label_cnf, text=lab_name)
            if input_key == "port" or input_key == "local_port":
                # 关于validatecommand设置，可参考http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/entry-validation.html
                tx = Entry(det_frm, det_text_cnf, validate="key", validatecommand=(is_int_valid_cmd, "%P"))
            elif input_key == "obfs":
                # Combobox: https://docs.python.org/3.1/library/tkinter.ttk.html#combobox
                tx = Combobox(det_frm, values=OBFS_LST, **det_combox_cnf)
            elif input_key == "method":
                tx = Combobox(det_frm, values=METHOD_LST, **det_combox_cnf)
            elif input_key == "protocol":
                tx = Combobox(det_frm, values=PROTOCOL_LST, **det_combox_cnf)
            elif input_key == "password":
                tx = Entry(det_frm, det_passwd_cnf)
            elif input_key == "ssr_url":
                tx = Entry(det_frm, textvariable=url_var, **det_text_readonly_cnf)
            else:
                tx = Entry(det_frm, det_text_cnf)
            det_input_widget_dict[input_key] = tx

            lb.grid(column=0, row=index)
            tx.grid(column=1, row=index)

        det_btn_frm = Frame(det_frm, frm_cnf, relief=FLAT)
        det_btn_frm.grid(row=12, column=0, columnspan=2)

        save_btn = Button(det_btn_frm, text="保存")
        link_btn = Button(det_btn_frm, textvariable=link_btn_var, bg=CONNECT_COLOR, activebackground=CONNECT_COLOR)

        save_btn.grid(row=0, column=0, padx=20)
        link_btn.grid(row=0, column=1, padx=20)

        link_btn.bind("<Button-1>", link_btn_click_handler)
        save_btn.bind("<Button-1>", save_btn_click_handler)

        return det_frm

    def menu_init(self):
        """菜单栏 初始化"""
        from gui.gui_funcs import encode_ssr_to_qr
        menu_bar = Menu(self.window)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="二维码导入")
        file_menu.add_command(label="二维码导出", command=encode_ssr_to_qr)
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
