from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QModelIndex
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
	def __init__(self, model):
		super().__init__()
		self.__mwui = Ui_MainWindow()
		self.__mwui.setupUi(self)
		self.model = model
		self.__mwui.tableView.setModel(self.model)
		self.__mwui.tableView.hideColumn(0)
		
		self.__mwui.tableView.clicked.connect(self.printIndex)
		self.__mwui.delBookButton.clicked.connect(self.deleteBook)
		self.__row = 0
		
	@Slot(QModelIndex)
	def printIndex(self, index):
		self.__row = index.row()
	
	@Slot()
	def deleteBook(self):
		self.model.removeRow(self.__row)
		self.model.select()
		

