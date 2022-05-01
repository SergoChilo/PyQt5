import json
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QAbstractItemView
from PyQt5.uic import loadUi

def registration_p():
    print('You are in sign up registration_p')
    dialog_create = Dialog_registration()
    widget.addWidget(dialog_create)
    widget.setCurrentIndex(widget.currentIndex() + 1)
def login():
    print('You are in sign in login')
    dialog_create = Dialog_login()
    widget.addWidget(dialog_create)
    widget.setCurrentIndex(widget.currentIndex() + 1)
def verification():
    print('You are in sign in verification')
    dialog_create = Dialog_verification()
    widget.addWidget(dialog_create)
    widget.setCurrentIndex(widget.currentIndex() + 1)
def admin():
    print('You are in sign in admin')
    dialog_create = Dialog_admin()
    widget.addWidget(dialog_create)
    widget.setCurrentIndex(widget.currentIndex() + 1)
def goto_main():
    print('You are in goto_main')
    main = main_window()
    widget.addWidget(main)
    widget.setCurrentIndex(widget.currentIndex() + 1)
def my_page():
    print('You are in goto_main')
    main = Dialog_my()
    widget.addWidget(main)
    widget.setCurrentIndex(widget.currentIndex() + 1)

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Main_menu.ui", self)
        self.pushButton.clicked.connect(registration_p)
        self.pushButton_2.clicked.connect(login)
        self.pushButton_3.clicked.connect(verification)
        self.pushButton_4.clicked.connect(login)
        self.pushButton_5.clicked.connect(self.close_)

    def close_(self, e):
        result = QtWidgets.QMessageBox.question(self, "Close Program",
                                                "Are you sure ?", QtWidgets.QMessageBox.Yes
                                                | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            exit(e)


def edit():
    lab = f'{Dialog_admin.listWidget.currentItem().text()}'
    with open(f'Files/{lab}') as file:
        data = json.load(file)
        Dialog_registration.lineEdit.setPlaceholderText(data["Name"])
        Dialog_registration.lineEdit_2.setPlaceholderText(data["Surname"])
        Dialog_registration.lineEdit_3.setPlaceholderText(data["Email"])
        Dialog_registration.lineEdit_4.setPlaceholderText(data["Login"])
        Dialog_registration.lineEdit_5.setPlaceholderText(data["Password"])
        # Dialog_registration.lineEdit.setText(data["Name"])
        # Dialog_registration.lineEdit_2.setText(data["Surname"])
        # Dialog_registration.lineEdit_3.setText(data["Email"])
        # Dialog_registration.lineEdit_4.setText(data["Login"])
        # Dialog_registration.lineEdit_5.setText(data["Password"])

        registration_p()

    file.close()


class Dialog_registration(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_registration.ui", self)
        self.lineEdit.setPlaceholderText("anun")
        self.lineEdit_2.setPlaceholderText("azganun")
        self.lineEdit_3.setPlaceholderText("mail@mail.ru")
        self.lineEdit_4.setPlaceholderText("A-Z, a-z, 0-9 ")
        self.lineEdit_5.setPlaceholderText("A-Z, a-z, 0-9")

        self.pushButton.clicked.connect(self.save_input_info)
        self.pushButton.clicked.connect(goto_main)
        self.pushButton_2.clicked.connect(goto_main)
        self.pushButton_3.clicked.connect(self.reset_)

    def reset_(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        print('File rested')
    def save_input_info(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        login = self.lineEdit_4.text()
        passw = self.lineEdit_5.text()
        data = ({
            'Name': name,
            'Surname': surname,
            'Email': email,
            'Login': login,
            'Password': passw
        })
        with open(f'Files/{name}.json', 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()
        print('Document saved')


class Dialog_login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_login.ui", self)

        self.pushButton.clicked.connect(self.verific)
        self.pushButton_2.clicked.connect(goto_main)
    def verific(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        profile_list = os.listdir('Files')
        for profile in profile_list:
            if username == profile[:-5]:
                with open(f'Files/{username}.json') as file:
                    data = json.load(file)
                    if username == 'admin' and password == 'admin':
                        admin()
                    elif password == data["Password"]:
                        my_page()
                        file.close()
                    elif username == 'admin' and password == 'admin':
                        admin()
                    else:
                        self.label.setText("Your password is wrong")
                        file.close()

            else:
                self.label.setText("Your username is wrong")

class Dialog_verification(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_verification.ui", self)

        self.pushButton.clicked.connect(self.push)
        self.pushButton_2.clicked.connect(goto_main)

    def push(self):
        profile_list = os.listdir('Files')
        username = self.lineEdit.text()
        for profile in profile_list:
            if username == profile[:-5]:
                with open(f'Files/{username}.json') as file:
                    data = json.load(file)
                    self.label_5.setText(data["Password"])
                    file.close()
            else:
                self.label_5.setText("Wrong username !!!")

class Dialog_admin(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_admin.ui", self)

        self.pushButton_4.clicked.connect(goto_main)
        profile_list = os.listdir('Files')
        for index, profile in enumerate(profile_list):
            if profile[-4:] == 'json':
                self.listWidget.insertItem(index, profile)

        # lab = f'{self.listWidget.currentItem().text()}'
        self.pushButton.clicked.connect(registration_p)
        self.pushButton_2.clicked.connect(edit)
        self.pushButton_3.clicked.connect(self.delete)

    def delete(self):
        lab = f'{self.listWidget.currentItem().text()}'
        os.remove(f'Files/{lab}')
        print('The file deleted')
        goto_main()



class Dialog_my(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_my.ui", self)
        self.pushButton.clicked.connect(login)




app = QApplication(sys.argv)
main = main_window()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
