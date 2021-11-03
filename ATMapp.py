#!/usr/bin/env python3

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

################## LOAD GUI ############################
from ATMgui import Ui_TechSealsATM

################## LOAD FUNCTION ############################
from functions import *


class MainWindow(QtWidgets.QMainWindow, Ui_TechSealsATM):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.atmui = Ui_TechSealsATM()
        self.atmui.setupUi (self)


        ############## PAGES NAVIGATION ########################
        ########################################################################
        #WELCOME PAGE
        self.atmui.startBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.languagePage))

        # LANGUAGE PAGE
        self.atmui.englishBtn.clicked.connect(lambda: UIFunctions.englishCode(self))
        self.atmui.twiBtn.clicked.connect(lambda: UIFunctions.twiCode(self))

      

#################### RUN PROGRAM ##########################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
