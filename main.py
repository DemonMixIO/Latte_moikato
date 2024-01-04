import sys

from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QStatusBar, QPlainTextEdit, QComboBox, \
    QPushButton, QFormLayout
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.editButton.setText(_translate("MainWindow", "Редактировать"))


class CoffeeApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Латте макиато")
        self.setGeometry(100, 100, 800, 600)

        self.tableWidget.setGeometry(0, 0, 800, 600)
        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)
        self.setup_table()

    def add(self):
        # print('add')
        self.add_form = AddWidget(self)
        self.add_form.show()

    def edit(self):
        # print('edit')
        self.selected_row = self.tableWidget.currentRow()
        if self.selected_row != -1:
            row = []
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(self.selected_row, col).text()
                row.append(item)
            # print(row)
            self.statusBar().showMessage('')
            self.edit_form = AddWidget(self, mode=self.selected_row, row=row)
            self.edit_form.show()

        else:
            self.statusBar().showMessage('Ничего не выбрано')

    def setup_table(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Сорт", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"])

        self.load_data()

    def load_data(self):
        connection = sqlite3.connect("release/data/coffee.sqlite")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM coffee")
        data = cursor.fetchall()

        connection.close()

        self.populate_table(data)

    def populate_table(self, data):
        self.tableWidget.setRowCount(len(data))

        for row_index, row_data in enumerate(data):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_index, col_index, item)


class Ui_AddWidget(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 231, 499))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.sort = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.sort.setObjectName("sort")
        self.horizontalLayout.addWidget(self.sort)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.pow = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.pow.setObjectName("pow")
        self.horizontalLayout_2.addWidget(self.pow)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.is_molotiy = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.is_molotiy.setObjectName("is_molotiy")
        self.horizontalLayout_3.addWidget(self.is_molotiy)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.taste_info = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.taste_info.setObjectName("taste_info")
        self.horizontalLayout_4.addWidget(self.taste_info)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.price = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.price.setObjectName("price")
        self.horizontalLayout_5.addWidget(self.price)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.size = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.size.setObjectName("size")
        self.horizontalLayout_6.addWidget(self.size)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AddWidget"))
        self.label_6.setText(_translate("MainWindow", "Сорт"))
        self.label_5.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_4.setText(_translate("MainWindow", "Молотый/в зернах"))
        self.label_3.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_2.setText(_translate("MainWindow", "цена"))
        self.label.setText(_translate("MainWindow", "Объем упаковки"))
        self.pushButton.setText(_translate("MainWindow", "Обновить"))


class AddWidget(QDialog, Ui_AddWidget):
    def __init__(self, parent=None, mode=-1, row=None):
        self.mode = mode
        self.row = row
        super().__init__(parent)
        self.setWindowTitle('Обновить')
        self.setFixedSize(300, 260)
        self.is_save = False
        self.setupUi(self)

        if self.mode == -1:
            self.statusbar = QStatusBar()
            self.sort = QPlainTextEdit()
            self.pow = QPlainTextEdit()
            self.is_molotiy = QPlainTextEdit()
            self.taste_info = QPlainTextEdit()
            self.price = QPlainTextEdit()
            self.size = QPlainTextEdit()
        else:
            # print(self.row)
            self.sort = QPlainTextEdit(self.row[1])
            self.pow = QPlainTextEdit(self.row[2])
            self.is_molotiy = QPlainTextEdit(self.row[3])
            self.taste_info = QPlainTextEdit(self.row[4])
            self.price = QPlainTextEdit(self.row[5])
            self.size = QPlainTextEdit(self.row[6])
            self.statusbar = QStatusBar()

        self.pushButton = QPushButton("Обновить")
        self.con = sqlite3.connect("release/data/coffee.sqlite")

        layout = QFormLayout()
        layout.addRow("Сорт:", self.sort)
        layout.addRow("Степень обжарки:", self.pow)
        layout.addRow("Молотый/в зернах:", self.is_molotiy)
        layout.addRow("Описание вкуса:", self.taste_info)
        layout.addRow("Цена:", self.price)
        layout.addRow("Объем упаковки:", self.size)
        layout.addRow(self.pushButton)
        layout.addRow(self.statusbar)

        self.pushButton.clicked.connect(self.save_record)

        self.setLayout(layout)

    def get_adding_verdict(self):
        return self.is_save

    def save_record(self):
        sort = self.sort.toPlainText()
        pow = self.pow.toPlainText()
        is_molotiy = self.is_molotiy.toPlainText()
        taste_info = self.taste_info.toPlainText()
        price = self.price.toPlainText()
        size = self.size.toPlainText()
        res = ''
        if self.mode == -1:
            res = (f"insert into coffee(sort, pow, is_molotiy, taste_info, price, size) values('{sort}', '{pow}',"
                   f" '{is_molotiy}', '{taste_info}', '{price}', '{size}')")
        else:
            res = (f"update coffee set sort='{sort}', pow={pow}, is_molotiy='{is_molotiy}', taste_info='{taste_info}',"
                   f" price={price}, size={size} where id = {self.row[0]}")

        if (all([sort, pow, is_molotiy, taste_info, price, size]) and pow.isdigit() and
                price.isdigit() and size.isdigit() and pow.isdigit()):
            self.is_save = True
            cur = self.con.cursor()
            cur.execute(res).fetchall()
            self.con.commit()
            self.parent().load_data()
            self.close()
        else:
            self.is_save = False
            self.statusbar.showMessage('Неверно заполнена форма')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
