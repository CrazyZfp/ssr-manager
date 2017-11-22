from tkinter import *
from gui.gui_config import *


def init():
    window = Tk()
    window.title("ssr-manager")
    window.geometry("900x400")
    window.resizable(width=False, height=False)

    win_frm = Frame(window)
    win_frm.pack()

    lst_frm = Frame(win_frm, cnf_frm, bg="black", width=280)  # 列表
    det_frm = Frame(win_frm, cnf_frm, bg="blue", width=340)  # 详情
    qr_frm = Frame(win_frm, cnf_frm, bg="green", width=280)  # 二维码

    lst_frm.pack(cnf_frm_pack)
    det_frm.pack(cnf_frm_pack)
    qr_frm.pack(cnf_frm_pack)

    window.mainloop()
