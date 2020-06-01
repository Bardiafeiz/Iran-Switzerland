# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_member_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 623)
        MainWindow.setStyleSheet("background-color:rgb(53, 53, 53)")
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
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
" min-height: 20px;\n"
" min-width: 20px;")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.id_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.id_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114);\n"
"")
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_lineEdit)
        self.name_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.name_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.title_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.title_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.title_lineEdit)
        self.company_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.company_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.company_lineEdit.setObjectName("company_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.company_lineEdit)
        self.activity_field_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.activity_field_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.activity_field_lineEdit.setObjectName("activity_field_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.activity_field_lineEdit)
        self.email_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.email_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.email_lineEdit)
        self.phone_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.phone_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.phone_lineEdit)
        self.mobile_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.mobile_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.mobile_lineEdit.setObjectName("mobile_lineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.mobile_lineEdit)
        self.address_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.address_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.address_lineEdit.setObjectName("address_lineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.address_lineEdit)
        self.submit_butt = QtWidgets.QPushButton(self.groupBox)
        self.submit_butt.setStyleSheet("background-color:rgb(206, 164, 114);\n"
"")
        self.submit_butt.setObjectName("submit_butt")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.submit_butt)
        self.back_butt = QtWidgets.QPushButton(self.groupBox)
        self.back_butt.setStyleSheet("background-color:rgb(206, 164, 114)")
        self.back_butt.setObjectName("back_butt")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.back_butt)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setStyleSheet("background-color:rgb(200, 149, 90);\n"
"border-radius: 10px;\n"
"min-height: 20px;\n"
"min-width: 20px;")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.fax_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.fax_lineEdit.setStyleSheet("background-color:rgb(206, 164, 114)")
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

