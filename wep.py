from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget
import main_menu, app, add_member_page, Table_widget
from pymongo import MongoClient
import socket, csv, os


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

    elif kind == 'question':
        massage_box.setIcon(QMessageBox.Critical)
        yes = massage_box.addButton('Yes', QMessageBox.YesRole)
        no = massage_box.addButton('No', QMessageBox.NoRole)
        massage_box.exec_()

        if massage_box.clickedButton() == yes:
            return True
        else:
            pass


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


class TablePage(QtWidgets.QMainWindow, Table_widget.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TablePage, self).__init__(parent)
        self.edit_buttons = []
        self.delete_buttons = []
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
        self.table_page.edit_buttons = []
        self.table_page.delete_buttons = []

        for i in range(row):
            # inserting members
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

            # inserting different buttons in the last column for each member
            edit_butt = QPushButton('Edit')
            delete_butt = QPushButton('Delete')
            self.table_page.edit_buttons.append(edit_butt)
            self.table_page.delete_buttons.append(delete_butt)

            hbox = QHBoxLayout()
            qwidget = QWidget()
            hbox.addWidget(edit_butt)
            hbox.addWidget(delete_butt)
            qwidget.setLayout(hbox)
            self.table_page.tableWidget.setCellWidget(i, 10, qwidget)

            self.table_page.edit_buttons[i].clicked.connect((lambda i=i: lambda: self.edit_butt_clicked(i))())
            self.table_page.delete_buttons[i].clicked.connect((lambda i=i: lambda: self.delete_butt_clicked(i))())

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
            self.pages.resize(1200, 620)
            self.pages.show()
        pass

    def connect_to_db(self):
        self.connection_alert()
        try:
            self.client = MongoClient("mongodb_address")
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
        pass
        # print(self.members[0].name, self.members[1].name)

    def submit_clicked(self):
        if self.db_connection and check_connection():
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

            self.insert_member(id, name, title, company, activity_field, email, phone, mobile, fax, address)
            self.load_page('app')
        else:
            show_alert("You should be connected to internet in order to make changes", 'w')

    def edit_butt_clicked(self, number):
        if self.db_connection and check_connection():
            if self.table_page.edit_buttons[number].text() == 'Edit':
                print(number)
                for i in range(10):
                    self.table_page.tableWidget.openPersistentEditor(self.table_page.tableWidget.item(number, i))
                self.table_page.edit_buttons[number].setText('Confirm')

            elif self.table_page.edit_buttons[number].text() == 'Confirm':
                id = self.table_page.tableWidget.item(number, 0).text()
                name = self.table_page.tableWidget.item(number, 1).text()
                title = self.table_page.tableWidget.item(number, 2).text()
                company = self.table_page.tableWidget.item(number, 3).text()
                activity_field = self.table_page.tableWidget.item(number, 4).text()
                email = self.table_page.tableWidget.item(number, 5).text()
                phone = self.table_page.tableWidget.item(number, 6).text()
                mobile = self.table_page.tableWidget.item(number, 7).text()
                fax = self.table_page.tableWidget.item(number, 8).text()
                address = self.table_page.tableWidget.item(number, 9).text()
                self.update_member(number, id, name, title, company, activity_field, email, phone, mobile, fax, address)
                self.table_page.edit_buttons[number].setText('Edit')
                for i in range(10):
                    self.table_page.tableWidget.closePersistentEditor(self.table_page.tableWidget.item(number, i))
        else:
            show_alert("You should be connected to internet in order to make changes", 'w')

    def delete_butt_clicked(self, number):
        if self.db_connection and check_connection():
            if show_alert("Are you sure?", 'question'):
                # delete from list
                del self.members[number]

                # delete from database
                self.rec.delete_one(list(self.rec.find())[number])

                self.load_page('table')
        else:
            show_alert("You should be connected to internet in order to make changes", 'w')

    # call it after finishing editing a member (id cannot be deleted)
    def update_member(self, number, id, name, title, company, activity_field, email, phone, mobile, fax, address):
        # update database
        updated_member_fields = {'id': id, 'name': name, 'title': title, 'company': company, 'activity field': activity_field,
                             'email': email, 'phone': phone, 'mobile': mobile, 'fax': fax, 'address': address }

        self.rec.update_one(list(self.rec.find())[number], {'$set': updated_member_fields})

        # update list
        updated_member = Member(id, name, title, company, activity_field, email, phone, mobile, fax, address)
        self.members[number] = updated_member

    # call it after submit butt clicked
    def insert_member(self, id, name, title, company, activity_field, email, phone, mobile, fax, address):
        # insert into database
        new_member = {'id': id, 'name': name, 'title': title, 'company': company, 'activity field': activity_field,
                          'email': email, 'phone': phone, 'mobile': mobile, 'fax': fax, 'address': address}
        self.rec.insert_one(new_member)

        # append to list
        member = Member(id, name, title, company, activity_field, email, phone, mobile, fax, address)
        self.members.append(member)

        # save on .csv file (locally)
        with open('Data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            [writer.writerow([member.id, member.name, member.title, member.company,
                              member.activity_field, member.email, member.phone,
                              member.mobile, member.fax, member.address])
             for member in self.members]

    def load_from_csv(self):
        try:
            with open('Data.csv', 'r') as file:
                data = csv.reader(file, delimiter=',')
                for row in data:
                    member = Member(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                    self.members.append(member)
        except:
            pass

    def load_from_database(self):
        try:
            members = list(self.rec.find())
            for member in members:
                id = member['id']
                name = member['name']
                title = member['title']
                company = member['company']
                activity_field = member['activity field']
                email = member['email']
                phone = member['phone']
                mobile = member['mobile']
                fax = member['fax']
                address = member['address']

                new_member = Member(id, name, title, company, activity_field, email, phone, mobile, fax, address)
                self.members.append(new_member)

        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = Start()
    sys.exit(app.exec_())

