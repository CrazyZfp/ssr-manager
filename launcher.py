from gui.gui_panel import App
from config_operator import read_config


def main():
    read_config()
    app = App()
    app.start()


if __name__ == "__main__":
    main()
