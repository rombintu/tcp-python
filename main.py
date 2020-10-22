import form
import socket
import sys
import datetime

from threading import Thread
from PyQt5 import QtWidgets


def Sending(message):
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.send(message.encode())
    sock.close()


class user:
    def __init__(self, name='Unknown'):
        self.name = name
    def setName(self, name):
        self.name = name

Client = user()

class App(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.push)

    def push(self):
        data = self.lineEdit.text()

        if data[0] == '!':
            name = data[1:]
            Client.setName(name)
            self.lineEdit.clear()
            msg = F'Ваше имя изменено на [{name}]'
            self.textBrowser.append(msg)
            return True

        today = datetime.datetime.today()
        hoursAndMinuts = "[" + today.strftime("%H:%M") + "]."
        message = hoursAndMinuts + Client.name + ': ' + data
        self.textBrowser.append(message)
        self.lineEdit.clear()

        Sending(message)

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    app.exec_()