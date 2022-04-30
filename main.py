import json
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QAbstractItemView
from PyQt5.uic import loadUi


def registration():
    pass


# def create_document():
#     print('You are in create_document')
#     dialog_create = Dialog_edit()
#     widget.addWidget(dialog_create)
#     widget.setCurrentIndex(widget.currentIndex() + 1)
#     dialog_create.create_doc()









def registration_p():
    print('You are in sign up')
    dialog_create = Dialog_registration()
    widget.addWidget(dialog_create)
    widget.setCurrentIndex(widget.currentIndex() + 1)
def login():
    print('You are in sign in')
    dialog_create = Dialog_login()
    widget.addWidget(dialog_create)
    widget.setCurrentIndex(widget.currentIndex() + 1)
def verification():
    print('You are in sign in')
    dialog_create = Dialog_verification()
    widget.addWidget(dialog_create)
    widget.setCurrentIndex(widget.currentIndex() + 1)
def admin():
    print('You are in sign in')
    dialog_create = Dialog_admin()
    widget.addWidget(dialog_create)
    widget.setCurrentIndex(widget.currentIndex() + 1)

def goto_main():
    print('You are in goto_main')
    main = main_window()
    widget.addWidget(main)
    widget.setCurrentIndex(widget.currentIndex() + 1)













class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("Main_menu.ui", self)
        # self.show()


        self.pushButton.clicked.connect(registration_p)
        self.pushButton_2.clicked.connect(login)
        self.pushButton_3.clicked.connect(verification)
        self.pushButton_4.clicked.connect(admin)
        self.pushButton_5.clicked.connect(self.close_)

    def close_(self, e):
        result = QtWidgets.QMessageBox.question(self, "Close Program",
                                                "Are you sure ?", QtWidgets.QMessageBox.Yes
                                                | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            exit(e)



class Dialog_registration(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_registration.ui", self)
        self.lineEdit.setPlaceholderText("anun")
        self.lineEdit_2.setPlaceholderText("azganun")
        self.lineEdit_3.setPlaceholderText("mail@mail.ru")
        self.lineEdit_4.setPlaceholderText("A-Z, a-z, 0-9 ")
        self.lineEdit_5.setPlaceholderText("A-Z, a-z, 0-9")

        self.pushButton_2.clicked.connect(goto_main)
        self.pushButton_3.clicked.connect(self.reset_)

    def reset_(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        print('File rested')
        ################################################
#   MY PAGE
    # def show_information(self):
    #     print('You are in show_information')
    #     self.label.setText(f'You selected : {self.listWidget.currentItem().text()}')
    #     self.lab = f'{self.listWidget.currentItem().text()}'
    #     with open(f'./Camera_profiles/{self.listWidget.currentItem().text()}') as file:
    #         data = json.load(file)
    #         self.label_10.setText(f'{self.listWidget.currentItem().text()[:-4]}')
    #         self.label_11.setText(data["Login"])
    #         self.label_12.setText(data["Password"])
    #         self.label_13.setText(data["Ip address"])
    #         self.label_17.setText(data["Port"])
    #         self.label_15.setText(data["Latitude"])
    #         self.label_16.setText(data["Longitude"])
    #         self.label_18.setText(data["Height"])
    #         file.close()
    #     print(f'show_information Selected element is {self.lab}')

    # def lineEdit_information(self):
    #     name = self.lineEdit.text()
    #     surname = self.lineEdit_2.text()
    #     email = self.lineEdit_3.text()
    #     login = self.lineEdit_4.text()
    #     passw = self.lineEdit_5.text()
        # data = ({
        #     'Name': name,
        #     'Surname': surname,
        #     'Email': email,
        #     'Login': login,
        #     'Password': passw
        # })
        # with open(f'{email}.txt', 'w') as outfile:
        #     json.dump(data, outfile)
        # outfile.close()
        # print('Document saved')
        #
        # print(login)

class Dialog_login(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_login.ui", self)
        self.pushButton_2.clicked.connect(goto_main)

class Dialog_verification(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_verification.ui", self)
        self.pushButton_2.clicked.connect(goto_main)

class Dialog_admin(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Dialog_admin.ui", self)

        self.pushButton_4.clicked.connect(goto_main)
    # profile_list = os.listdir('Camera_profiles')
    #         for index, profile in enumerate(profile_list):
    #             if profile[-3:] == 'txt':
    #                 self.listWidget.insertItem(index, profile)


app = QApplication(sys.argv)
main = main_window()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
