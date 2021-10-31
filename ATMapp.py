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

        # LOGIN PAGE
        #self.atmui.loginBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.menuPage))
        self.atmui.cardlessBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.momomenuPage))

        # FORGOT PIN PAGE
        self.atmui.fpYesBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.verificationcodePage))
        self.atmui.fpNoBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.exitPage))

        # VERIFICATION CODE PAGE
        self.atmui.vericodeSubmitBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.pinchangePage))
        
        # MAIN MENU PAGE
        self.atmui.balanceBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.balancePage))
        self.atmui.withdrawalBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.withdrawalcurrencyPage))
        self.atmui.momoBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.momomenuPage))
        self.atmui.logoutBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.confirmquitPage))

        # DONE BUTTONS
        self.atmui.backtoMenuBtn2.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.newtransactionPage))
        self.atmui.backtoMenuBtn3.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.newtransactionPage))
        self.atmui.backtoMenuBtn4.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.newtransactionPage))

        # WITHDRAWAL CURRENCY PAGE
        self.atmui.cediBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.withdrawalamountPage))
        self.atmui.dollarBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.withdrawalamountPage))

        # WITHDRAWAL AMOUNT PAGE
        self.atmui.withdrawalSubmitBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.confirmwithdrawalPage))

        # CONFIRM WITHDRAWAL PAGE
        self.atmui.confirmwithdrawYesBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.successfulwithdrawalPage))
        self.atmui.confirmwithdrawNoBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.withdrawalcurrencyPage))

        # SUCCESSFUL WITHDRAWAL PAGE
        self.atmui.receiptoptionBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.receiptrequestPage))

        # RECEIPT REQUEST PAGE
        self.atmui.confirmreceiptYesBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.receiptPage))
        self.atmui.confirmreceiptNoBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.newtransactionPage))

        # NEW TRANSACTION PAGE
        self.atmui.newtransactionYesBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.menuPage))
        self.atmui.newtransactionNoBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.confirmquitPage))

        # MOMO MENU
        self.atmui.mainmenuBtn2.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.menuPage))
        self.atmui.airtelBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.transactioncodePage))
        self.atmui.mtnBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.transactioncodePage))
        self.atmui.vodafoneBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.transactioncodePage))

        # TRANSACTION CODE PAGE
        self.atmui.transcodeSubmitBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.momowithdrawPage))

        # MOMO WITHDRAWAL PAGE
        self.atmui.momowithdrawSubmitBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.momoconfirmPage))

        # MOMO WITHDRAWAL CONFIRMATION PAGE
        self.atmui.momoconfirmwithdrawYesBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.momopinPage))
        self.atmui.momoconfirmwithdrawNoBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.momomenuPage))
        self.atmui.momopinSubmitBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.momosuccessPage))

        # LOGOUT CONFIRM PAGE
        self.atmui.confirmquitYesBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.exitPage))
        self.atmui.confirmquitNoBtn.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.menuPage))
        



#################### RUN PROGRAM ##########################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


