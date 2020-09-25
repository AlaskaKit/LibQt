import sys

from PySide2.QtWidgets import QApplication
from lib_widgets import MainWindow
from db_initializing import *


def main(argv):
    app = QApplication(argv)
    model = DBBuilder.build()
    m_window = MainWindow(model)
    m_window.show()
    

    return app.exec_()


if __name__ == '__main__':
    exit_status = main(sys.argv)
    sys.exit(exit_status)
