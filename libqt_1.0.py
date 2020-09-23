import sys

from PySide2.QtWidgets import QApplication
from lib_widgets import MainWindow


def main(argv):
    app = QApplication(argv)
    # model = DBBuilder.build()
    m_window = MainWindow()
    m_window.show()
    

    return app.exec_()


if __name__ == '__main__':

    # os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'

    exit_status = main(sys.argv)
    sys.exit(exit_status)