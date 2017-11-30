from gui.gui_panel import App
from config_operator import ssr_path_verify


def __main__():
    ssr_path_verify()

    app = App()
    window = app.window
    window.mainloop()


if __name__ == "__main__":
    __main__()
