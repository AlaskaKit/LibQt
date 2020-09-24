import sys

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QModelIndex, Qt
from PySide2.QtSql import QSqlTableModel, QSqlRecord, QSqlField, QSqlDatabase, QSqlQuery
from PySide2.QtWidgets import QApplication


class Book:
	def __init__(self, title, author, year):
		self.id = None
		self.author = author
		self.title = title
		self.year = year


class MyTableModel(QSqlTableModel):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
	def flags(self, index: QModelIndex):
		return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
	
	def addBook(self, book: Book):
		
		rowCount = self.rowCount()
		book_record = QSqlRecord()
		
		id_table = QSqlField("id", int)
		id_table.setAutoValue(True)
		book_record.insert(0, id_table)
		
		author = QSqlField("author", str)
		author.setValue(book.author)
		book_record.insert(1, author)
		
		title = QSqlField("title", str)
		title.setValue(book.title)
		book_record.insert(2, title)
		
		year = QSqlField("year", str)
		year.setValue(book.year)
		book_record.insert(3, year)
		
		self.insertRecord(rowCount, book_record)
		self.select()
		
		index = self.createIndex(0, 1)
		print(self.data(index))
	
	def searchBook(self, book):
		index = self.createIndex(2, 0)
		print(self.data(index))
		
		
class DBBuilder:
	@staticmethod
	def build():
		# Дополнительный путь к SQL драйверу
		QApplication.setLibraryPaths(['./platforms', './plugins', QApplication.libraryPaths()[2]])
		
		db = QSqlDatabase.addDatabase('QSQLITE')
		db.setDatabaseName('db_lib.db3')
		
		if not db.open():
			print('БД не существует')
			sys.exit(-1)
		
		model = MyTableModel(None, db)
		
		if 'mytable' not in db.tables():
			query = QSqlQuery()
			query.exec_(
				"create table mytable(id integer primary key autoincrement, author text, title text, year text)")
		
		model.setTable('mytable')
		model.setEditStrategy(QSqlTableModel.OnFieldChange)
		
		model.select()
		model.setHeaderData(0, Qt.Horizontal, "id")
		model.setHeaderData(1, Qt.Horizontal, "author")
		model.setHeaderData(2, Qt.Horizontal, "title")
		model.setHeaderData(3, Qt.Horizontal, "year")
		
		return model
