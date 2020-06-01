# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 364)
        MainWindow.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.proceedButt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceedButt.sizePolicy().hasHeightForWidth())
        self.proceedButt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.proceedButt.setFont(font)
        self.proceedButt.setObjectName("proceedButt")
        self.gridLayout_2.addWidget(self.proceedButt, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.passLine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passLine.sizePolicy().hasHeightForWidth())
        self.passLine.setSizePolicy(sizePolicy)
        self.passLine.setObjectName("passLine")
        self.gridLayout_2.addWidget(self.passLine, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuAutosave_3 = QtWidgets.QMenu(self.menuFile)
        self.menuAutosave_3.setObjectName("menuAutosave_3")
        self.menuAutosave = QtWidgets.QMenu(self.menubar)
        self.menuAutosave.setObjectName("menuAutosave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionin_database = QtWidgets.QAction(MainWindow)
        self.actionin_database.setObjectName("actionin_database")
        self.actionin_local_file_csv = QtWidgets.QAction(MainWindow)
        self.actionin_local_file_csv.setObjectName("actionin_local_file_csv")
        self.actionOn = QtWidgets.QAction(MainWindow)
        self.actionOn.setObjectName("actionOn")
        self.actionOff = QtWidgets.QAction(MainWindow)
        self.actionOff.setObjectName("actionOff")
        self.actionboth = QtWidgets.QAction(MainWindow)
        self.actionboth.setObjectName("actionboth")
        self.menuSave.addSeparator()
        self.menuSave.addAction(self.actionin_database)
        self.menuSave.addAction(self.actionin_local_file_csv)
        self.menuSave.addAction(self.actionboth)
        self.menuAutosave_3.addAction(self.actionOn)
        self.menuAutosave_3.addAction(self.actionOff)
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addAction(self.menuAutosave_3.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAutosave.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.proceedButt.setText(_translate("MainWindow", "Proceed"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuAutosave_3.setTitle(_translate("MainWindow", "Autosave"))
        self.menuAutosave.setTitle(_translate("MainWindow", "Autosave"))
        self.actionin_database.setText(_translate("MainWindow", "in database"))
        self.actionin_local_file_csv.setText(_translate("MainWindow", "in local file (.csv)"))
        self.actionOn.setText(_translate("MainWindow", "On"))
        self.actionOff.setText(_translate("MainWindow", "Off"))
        self.actionboth.setText(_translate("MainWindow", "both"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.add_member_butt = QtWidgets.QPushButton(self.centralwidget)
        self.add_member_butt.setObjectName("add_member_butt")
        self.gridLayout_3.addWidget(self.add_member_butt, 2, 1, 1, 1)
        self.show_table_butt = QtWidgets.QPushButton(self.centralwidget)
        self.show_table_butt.setObjectName("show_table_butt")
        self.gridLayout_3.addWidget(self.show_table_butt, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 22))
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
        self.add_member_butt.setText(_translate("MainWindow", "Add Member"))
        self.show_table_butt.setText(_translate("MainWindow", "Show Table"))




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.id_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_lineEdit)
        self.name_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.title_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.title_lineEdit)
        self.company_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.company_lineEdit.setObjectName("company_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.company_lineEdit)
        self.activity_field_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.activity_field_lineEdit.setObjectName("activity_field_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.activity_field_lineEdit)
        self.email_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.email_lineEdit)
        self.phone_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.phone_lineEdit)
        self.mobile_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.mobile_lineEdit.setObjectName("mobile_lineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.mobile_lineEdit)
        self.address_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.address_lineEdit.setObjectName("address_lineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.address_lineEdit)
        self.submit_butt = QtWidgets.QPushButton(self.groupBox)
        self.submit_butt.setObjectName("submit_butt")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.submit_butt)
        self.back_butt = QtWidgets.QPushButton(self.groupBox)
        self.back_butt.setObjectName("back_butt")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.back_butt)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.fax_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.fax_lineEdit.setObjectName("fax_lineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.fax_lineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
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
        self.label.setText(_translate("MainWindow", "Membership ID"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Title"))
        self.label_4.setText(_translate("MainWindow", "Company"))
        self.label_5.setText(_translate("MainWindow", "Activity Field"))
        self.label_6.setText(_translate("MainWindow", "Email"))
        self.label_7.setText(_translate("MainWindow", "Phone"))
        self.label_8.setText(_translate("MainWindow", "Mobile"))
        self.label_9.setText(_translate("MainWindow", "Address"))
        self.submit_butt.setText(_translate("MainWindow", "Submit"))
        self.back_butt.setText(_translate("MainWindow", "Back"))
        self.label_10.setText(_translate("MainWindow", "Fax"))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_and_save_butt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_and_save_butt.sizePolicy().hasHeightForWidth())
        self.edit_and_save_butt.setSizePolicy(sizePolicy)
        self.edit_and_save_butt.setObjectName("edit_and_save_butt")
        self.gridLayout.addWidget(self.edit_and_save_butt, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.back_butt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_butt.sizePolicy().hasHeightForWidth())
        self.back_butt.setSizePolicy(sizePolicy)
        self.back_butt.setObjectName("back_butt")
        self.gridLayout.addWidget(self.back_butt, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 22))
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
        self.edit_and_save_butt.setText(_translate("MainWindow", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Membership ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Company"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Activity Field"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Mobile"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Address"))
        self.back_butt.setText(_translate("MainWindow", "Back"))


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import Table_Widget
from pymongo import MongoClient
import socket, pickle, csv, os
import main_menu, app, Table_Widget, add_member_page


def check_connection():
    try:
        socket.create_connection(('Google.com', 80))
    except :
        return False
    return True


def show_alert(text, kind):
    massage_box = QMessageBox()
    massage_box.setWindowTitle("Error")
    massage_box.setText(text)
    if kind == 'i':
        massage_box.setIcon(QMessageBox.Information)
        x = massage_box.exec_()
    elif kind == 'w':
        massage_box.setIcon(QMessageBox.Warning)
        x = massage_box.exec_()
    elif kind == 'connection':
        massage_box.setIcon(QMessageBox.Critical)
        offline = massage_box.addButton('Proceed offline', QMessageBox.YesRole)
        retry = massage_box.addButton('Retry', QMessageBox.NoRole)
        massage_box.exec_()

        if massage_box.clickedButton() == offline:
            return True


# Create a class for each ui page
class MainPage(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)


class AppPage(QtWidgets.QMainWindow, app.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AppPage, self).__init__(parent)
        self.setupUi(self)


class AddMemberPage(QtWidgets.QMainWindow, add_member_page.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AddMemberPage, self).__init__(parent)
        self.setupUi(self)


class TablePage(QtWidgets.QMainWindow, Table_Widget.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TablePage, self).__init__(parent)
        self.setupUi(self)


class Member:
    def __init__(self, id, name, title, company, activity_field, email, phone, mobile, fax, address):
        self.id = id
        self.name = name
        self.title = title
        self.company = company
        self.activity_field = activity_field
        self.email = email
        self.phone = phone
        self.mobile = mobile
        self.fax = fax
        self.address = address


class Start:
    def __init__(self):
        self.members = []
        self.db_connection = False
        self.init()
        self.load_page('main')
        self.manage()

    def load_all_pages(self):
        self.main_page = MainPage()
        self.app_page = AppPage()
        self.add_member_page = AddMemberPage()
        self.table_page = TablePage()
        self.pages = QtWidgets.QStackedWidget()
        self.pages.addWidget(self.main_page)
        self.pages.addWidget(self.app_page)
        self.pages.addWidget(self.add_member_page)
        self.pages.addWidget(self.table_page)

    def main_page_preparations(self):
        pass

    def app_page_preparations(self):
        pass

    def add_member_page_preparations(self):
        pass

    def table_page_preparations(self):
        row = len(self.members)
        self.table_page.tableWidget.setRowCount(row)

        for i in range(row):
            self.table_page.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.members[i].id)))
            self.table_page.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.members[i].name)))
            self.table_page.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.members[i].title)))
            self.table_page.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.members[i].company)))
            self.table_page.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.members[i].activity_field)))
            self.table_page.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.members[i].email)))
            self.table_page.tableWidget.setItem(i, 6, QTableWidgetItem(str(self.members[i].phone)))
            self.table_page.tableWidget.setItem(i, 7, QTableWidgetItem(str(self.members[i].mobile)))
            self.table_page.tableWidget.setItem(i, 8, QTableWidgetItem(str(self.members[i].fax)))
            self.table_page.tableWidget.setItem(i, 9, QTableWidgetItem(str(self.members[i].address)))

            self.table_page.tableWidget.resizeColumnsToContents()
            self.table_page.tableWidget.resizeRowsToContents()

    def load_page(self, page_name):
        if page_name == 'main':
            self.main_page_preparations()
            self.pages.setCurrentIndex(0)
            self.pages.resize(800, 100)
            self.pages.show()
        elif page_name == 'app':
            self.app_page_preparations()
            self.pages.setCurrentIndex(1)
            self.pages.resize(800, 100)
            self.pages.show()
        elif page_name == 'add member':
            self.add_member_page_preparations()
            self.pages.setCurrentIndex(2)
            self.pages.resize(900, 575)
            self.pages.show()
        elif page_name == 'table':
            self.table_page_preparations()
            self.pages.setCurrentIndex(3)
            self.pages.resize(800, 620)
            self.pages.show()


    def connect_to_db(self):
        self.connection_alert()
        try:
            self.client = MongoClient("mongodb+srv://Bardia:npe221@cluster0-iou38.mongodb.net/test?retryWrites=true&w=majority")
            print("connected!")
            self.db_connection = True
        except:
            self.db_connection = False
            print("connection failed")

    def connection_alert(self):
        while not check_connection():
            if show_alert('Please make sure you are connected to internet', 'connection'):
                break

    def init(self):
        # load pages and set functionality to their buttons and other widgets
        self.load_all_pages()
        self.main_page.proceedButt.clicked.connect(lambda: self.load_page('app'))
        self.add_member_page.back_butt.clicked.connect(lambda: self.load_page('app'))
        self.table_page.back_butt.clicked.connect(lambda: self.load_page('app'))
        self.app_page.show_table_butt.clicked.connect(lambda: self.load_page('table'))
        self.app_page.add_member_butt.clicked.connect(lambda: self.load_page('add member'))
        self.add_member_page.submit_butt.clicked.connect(self.submit_clicked)

        # database connection preparations
        self.connect_to_db()
        if self.db_connection:
            self.db = self.client.get_database('Iran_Switzerland_db')
            self.rec = self.db.person

        # load the data considering whether we are connected to database or not
        if self.db_connection:
            self.load_from_database()
        else:
            self.load_from_csv()

    def manage(self):
        print(self.members[0].name, self.members[1].name)

    def submit_clicked(self):
        id = str(self.add_member_page.id_lineEdit.text())
        name = str(self.add_member_page.name_lineEdit.text())
        title = str(self.add_member_page.title_lineEdit.text())
        company = str(self.add_member_page.company_lineEdit.text())
        activity_field = str(self.add_member_page.activity_field_lineEdit.text())
        email = str(self.add_member_page.email_lineEdit.text())
        phone = str(self.add_member_page.phone_lineEdit.text())
        mobile = str(self.add_member_page.mobile_lineEdit.text())
        fax = str(self.add_member_page.fax_lineEdit.text())
        address = str(self.add_member_page.address_lineEdit.text())

        member = Member(id, name, title, company, activity_field, email, phone, mobile, fax, address)
        self.members.append(member)

        self.save_everywhere()
        self.load_page('app')

    def save_everywhere(self):
        # save into database
        dumped = pickle.dumps(self.members)
        data = list(self.rec.find())
        if len(data) == 0:
            self.rec.insert_one({'data': dumped})
        else:
            self.rec.update_one(data[0], {'$set': {'data': dumped}})

        # save into .csv file (locally)
        with open('Data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            [writer.writerow([member.id, member.name, member.title, member.company,
                              member.activity_field, member.email, member.phone,
                              member.mobile, member.fax, member.address])
             for member in self.members]

    def load_from_csv(self):
        with open('Data.csv', 'r') as file:
            data = csv.reader(file, delimiter=',')
            for row in data:
                member = Member(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                self.members.append(member)

    def load_from_database(self):
        self.members = pickle.loads(list(self.rec.find())[0]['data'])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = Start()
    sys.exit(app.exec_())

