from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
	def __init__(self, model):
		super().__init__()
		self.__mwui = Ui_MainWindow()
		self.__mwui.setupUi(self)
		self.model = model
		self.tableView.setModel(self.model)
		self.tableView.hideColumn(0)

