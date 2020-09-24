from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QModelIndex, Qt
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QWidget
from ui_addbook import Ui_Form
from ui_filterbook import Ui_Form2
from db_initializing import Book


class AddBookWidget(QWidget):
    def __init__(self, model):
        super().__init__()
        self.__addui = Ui_Form()
        self.__addui.setupUi(self)
        self.model = model
        self.__addui.pushButton.clicked.connect(self.addition)
        self.__addui.pushButton_2.clicked.connect(self.closing)
        
    @Slot()
    def addition(self):
        book = Book(self.__addui.lineEdit.text(), self.__addui.lineEdit_2.text(), self.__addui.lineEdit_3.text())
        self.model.addBook(book)
        self.model.select()
        
    @Slot()
    def closing(self):
        self.close()


class FilterBookWidget(QWidget):
    def __init__(self, model):
        super().__init__()
        self.__fltr = Ui_Form2()
        self.__fltr.setupUi(self)
        self.model = model
        self.__fltr.pushButton.clicked.connect(self.apply)
        self.__fltr.pushButton_2.clicked.connect(self.reset)
        self.__fltr.pushButton_3.clicked.connect(self.closing)
        self.__fltr.radioButton.setChecked(True)
        
    @Slot()
    def apply(self):
        column = ""
        if self.__fltr.radioButton.isChecked():
            column = "author"
        elif self.__fltr.radioButton_2.isChecked():
            column = "title"
        elif self.__fltr.radioButton_3.isChecked():
            column = "year"
        text = self.__fltr.lineEdit.text()
        self.model.setFilter(f'{column} = "{text}"')
        self.model.select()

    @Slot()
    def reset(self):
        self.model.setFilter('')
        self.model.select()
    
    @Slot()
    def closing(self):
        self.close()

     
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
        self.__mwui.searchBookButton.clicked.connect(self.searchBook)
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

    @Slot()
    def searchBook(self):
        self.fltrwidget = FilterBookWidget(self.model)
        fltr_w = self.fltrwidget
        fltr_w.show()
        
        
        
        

