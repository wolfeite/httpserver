from libs.http import createFlaskApp
from app import config_app
import sys
from PyQt5.QtWidgets import QApplication
from gui import Gui

if __name__ == "__main__":
    gui = Gui()
    QApp = QApplication(sys.argv)
    gui.init()
    # httpApp = create_http_app(gui)
    httpApp = createFlaskApp({"host": "0.0.0.0", "debug": False, "port": 3100}, template_folder="data/view",
                             static_folder="data/statics")
    httpApp.attr = ("gui", gui)
    config_app(httpApp)
    sys.exit(QApp.exec_())
