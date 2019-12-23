#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.initButton()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Example')
        # self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()

    def initButton(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip(
            'This is a <b>QPushButton</b> widget and it exits the program.')
        btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.clicked.connect(self.closeEvent)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QMessageBox.Yes |
                                           QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
