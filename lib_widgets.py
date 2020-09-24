from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QModelIndex
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QWidget
from ui_addbook import Ui_Form
from db_loading import Book


class AddBookWidget(QWidget):
    def __init__(self, model):
        super().__init__()
        self.__addui = Ui_Form()
        self.__addui.setupUi(self)
        self.__addui.pushButton.clicked.connect(self.addition)
        
    @Slot()
    def addition(self):
        book = Book(self.titleEdit.text(), self.authorEdit.text(), self.yearEdit.text())
        self.model.addBook(book)
        
        


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
        self.__mwui.addBookButton.clicked.connect(self.addBook)
        self.__row = 0
        
    @Slot(QModelIndex)
    def printIndex(self, index):
        self.__row = index.row()
    
    @Slot()
    def deleteBook(self):
        self.model.removeRow(self.__row)
        self.model.select()
    
    @Slot()
    def addBook(self):
        self.addwidget = AddBookWidget(self.model)
        add_w = self.addwidget
        add_w.show()
        
        

