# -*- coding: utf-8 -*-
# __author__ = 'Lu'
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon
from myui import Ui_Form
class myWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        # self.buton=QPushButton(self)
        # self.buton.setIcon(QIcon('./res/picture/001.jpg'))
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    myshow=myWindow()
    sys.exit(app.exec_())