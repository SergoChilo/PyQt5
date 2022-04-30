import json
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QAbstractItemView
from PyQt5.uic import loadUi

import sys


def registration():
    pass


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        loadUi("untitled.ui", self)
        self.show()
        self.lineEdit.setPlaceholderText("Ara")
        self.lineEdit_2.setPlaceholderText("B****yan")
        self.lineEdit_3.setPlaceholderText("ara@araofficial.com")
        self.lineEdit_4.setPlaceholderText("A-Z, a-z, 0-9 ")
        self.lineEdit_5.setPlaceholderText("A-Z, a-z, 0-9")
        self.pushButton.clicked.connect(self.lineEdit_information)

    def lineEdit_information(self):
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
        with open(f'{email}.txt', 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()
        print('Document saved')

        print(login)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
