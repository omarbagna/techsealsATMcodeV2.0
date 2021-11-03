from ATMapp import *
from functional import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class UIFunctions(MainWindow):
    global sessiondata

    def loginfunction(self):
        
        global sessiondata

        userName = self.atmui.usernameInput.text()
        pin = self.atmui.loginpinInput.text()
        sessiondata =userLogin(userName)
        
        userPin = str(sessiondata['pin'])
        

        verify = pinVerify(userPin, pin)
        if verify == True:
            self.atmui.welcomeTitle.setText("Welcome "+ userName.upper())
            UIFunctions.Menufunction(self)
            
        else : 
            # pop up for wrong logins 
            self.atmui.englishBtn.clicked.connect(lambda: UIFunctions.englishCode(self))
        
        

    def Menufunction(self):
        self.atmui.main.setCurrentWidget(self.atmui.menuPage)

    
        
    

    def englishCode(self):

        ############################## ATM MENU PAGE #############################
        ################################ TITLE TEXT ##############################
        ##########################################################################
        
        self.atmui.main.setCurrentWidget(self.atmui.loginPage)

        
        self.atmui.loginBtn.clicked.connect(lambda:  UIFunctions.loginfunction(self))
        name = UIFunctions.loginfunction
        print(name)
        
        #userBalance=sessiondata['balance']
        
        

        
        
        
        self.atmui.balanceBtn.clicked.connect(lambda:UIFunctions.BalFunction(self))

        


        #sessiondata = userLogin(self.atmui.usernameInput.text())
        # RETRIEVE SPECIFIED USER BALANCE AND STORE TO VARIABLE
        #userBalance = sessiondata['balance']

        #self.balanceText.setText(_translate("TechSealsATM", "Your current GHS balance is\n"
        #"GHS" + userBalance['GHS'] + "\n""USD" + userBalance['USD'] ))

        return 
    def BalFunction(self):
            userBalance = sessiondata['balance']
            GHS= userBalance["GHS"]
            USD= userBalance["USD"]
            self.atmui.main.setCurrentWidget(self.atmui.balancePage)

            statement = "Your available balance in \n""GHS : " + str(GHS) + "\n""USD : " + str(USD)
            self.atmui.balanceText.setText(statement )

    def twiCode(self):

        #TRANSLATE ALL TEXT TO TWI

        ################################ LOGIN PAGE ##############################
        ############################# LOGIN BUTTON TEXT ##########################
        ##########################################################################
        self.atmui.loginBtn.setText("TOASO")

        ################################ LOGIN PAGE ##############################
        ########################### CARDLESS BUTTON TEXT #########################
        ##########################################################################
        self.atmui.cardlessBtn.setText("Cardless Service")

        ################################ LOGIN PAGE ##############################
        ################################ TITLE TEXT ##############################
        ##########################################################################
        self.atmui.loginTitle.setText("WO KRATAA")

        ################################ LOGIN PAGE ##############################
        #################### USERNAME INPUT PLACEHOLDER TEXT #####################
        ##########################################################################
        self.atmui.usernameInput.setPlaceholderText("BƆ WO DIN")

        ################################ LOGIN PAGE ##############################
        ######################## PIN INPUT PLACEHOLDER TEXT ######################
        ##########################################################################
        self.atmui.loginpinInput.setPlaceholderText("BƆ WO PIN")


        ############################ FORGOT PIN PAGE #############################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.atmui.forgotpinTitle.setText("Woafiri wo pin anaa?")

        ############################ FORGOT PIN PAGE #############################
        ############################ NO BUTTON TEXT ##############################
        ##########################################################################
        self.atmui.fpNoBtn.setText("DAABI")

        ############################ FORGOT PIN PAGE #############################
        ############################ Yes BUTTON TEXT #############################
        ##########################################################################
        self.atmui.fpYesBtn.setText("AANE")

        ############################ FORGOT PIN PAGE #############################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.atmui.forgotpinText.setText("Wo pɛ sɛ wo sesa wo PIN anaa?")


        ######################## VERIFICATION CODE PAGE ##########################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.atmui.verificationcodeTitle.setText("VERIFICATION CODE")

        ######################## VERIFICATION CODE PAGE ##########################
        ################################ CODE TEXT ###############################
        ##########################################################################
        self.atmui.verificationcodeText.setText("682386")

        ######################## VERIFICATION CODE PAGE ##########################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.atmui.vericodeParagraph.setText("Yɛ a mane Verification Code no \nwɔ wo fon no so")
        
        ######################## VERIFICATION CODE PAGE ##########################
        ########################### INSTRUCTION TEXT #############################
        ##########################################################################
        self.atmui.vericodeInputTitle.setText("Bɔ wo CODE no wɔ ha")

        ######################## VERIFICATION CODE PAGE ##########################
        ##################### CODE INPUT PLACEHOLDER TEXT ########################
        ##########################################################################
        self.atmui.verificationcodeInput.setPlaceholderText("VERIFICATION CODE")

        ######################## VERIFICATION CODE PAGE ##########################
        ########################## Submit BUTTON TEXT ############################
        ##########################################################################
        self.atmui.vericodeSubmitBtn.setText("MANE")


        ############################## PIN CHANGE PAGE ###########################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.atmui.pinchangeTitle.setText("PIN NSESAEƐ")

        ############################## PIN CHANGE PAGE ###########################
        ############################ CONFIRM BUTTON TEXT #########################
        ##########################################################################
        self.atmui.pinchangeConfirmBtn.setText("WIE")

        ############################## PIN CHANGE PAGE ###########################
        ########################## NEW PIN PLACEHOLDER TEXT ######################
        ##########################################################################
        self.atmui.newpinInput.setPlaceholderText("BƆ PIN FOFORƆ")

        ############################## PIN CHANGE PAGE ###########################
        ##################### RE-ENTER NEW PIN PLACEHOLDER TEXT ##################
        ##########################################################################
        self.atmui.newpinconfirmInput.setPlaceholderText("SAN BƆ PIN NO")


        ############################## ATM MENU PAGE #############################
        ################################ TITLE TEXT ##############################
        ##########################################################################
        self.atmui.welcomeTitle.setText("Akwaaba "+UIFunctions.data()['name'])

        ############################## ATM MENU PAGE #############################
        ################################# BODY TEXT ##############################
        ##########################################################################
        self.atmui.welcomeText.setText("Deɛn na wo pɛsɛ wo yɛ ɛnnɛ?")

        ############################## ATM MENU PAGE #############################
        ########################### BALANCE BUTTON TEXT ##########################
        ##########################################################################
        self.atmui.balanceBtn.setText("Hwɛ wo sika")

        ############################## ATM MENU PAGE #############################
        ######################### WITHDRAWAL BUTTON TEXT #########################
        ##########################################################################
        self.atmui.withdrawalBtn.setText("Yi sika")

        ############################## ATM MENU PAGE #############################
        ############################ MOMO BUTTON TEXT ############################
        ##########################################################################
        self.atmui.momoBtn.setText("Mobile Money")

        ############################## ATM MENU PAGE #############################
        ############################ LOGOUT BUTTON TEXT ##########################
        ##########################################################################
        self.atmui.logoutBtn.setText("PUE")


        ######################## WITHDRAWAL CURENCY PAGE #########################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.atmui.withdrawalcurrencyTitle.setText("YI SIKA")

        ######################## WITHDRAWAL CURENCY PAGE #########################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.atmui.withdrawalcurrencyText.setText("Yi fri Ghana Cedi anaa US Dollar account mu")
        
        ######################## WITHDRAWAL CURENCY PAGE #########################
        ########################### CEDI BUTTON TEXT #############################
        ##########################################################################
        self.atmui.cediBtn.setText("GHS")

        ######################## WITHDRAWAL CURENCY PAGE #########################
        ########################## DOLLAR BUTTON TEXT ############################
        ##########################################################################
        self.atmui.dollarBtn.setText("USD")


        ######################### WITHDRAWAL AMOUNT PAGE #########################
        ############################# CURRENCY TEXT ##############################
        ##########################################################################
        self.atmui.currencyText.setText("GHS")

        ######################### WITHDRAWAL AMOUNT PAGE #########################
        ########################### Submit BUTTON TEXT ###########################
        ##########################################################################
        self.atmui.withdrawalSubmitBtn.setText("MANE")

        ######################### WITHDRAWAL AMOUNT PAGE #########################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.atmui.withdrawalamountTitle.setText("Bɔ sika dodow a wopɛ \nsɛ woyi")


        ######################## CONFIRM WITHDRAWAL PAGE #########################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.atmui.confirmwithdrawalText.setText("Mepakyɛw hwɛ sɛ sika no aso GHS 1000")

        ######################## CONFIRM WITHDRAWAL PAGE #########################
        ############################ Yes BUTTON TEXT #############################
        ##########################################################################
        self.atmui.confirmwithdrawYesBtn.setText("AANE")

        ######################## CONFIRM WITHDRAWAL PAGE #########################
        ############################# NO BUTTON TEXT #############################
        ##########################################################################
        self.atmui.confirmwithdrawNoBtn.setText("DAABI")


        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ######################### WITHDRAWAL AMOUNT TEXT #########################
        ##########################################################################
        self.atmui.withdrawnamountText.setText("Watumi ayi GHS 1000")

        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ########################## PREVIOUS BALANCE TEXT #########################
        ##########################################################################
        self.atmui.previousbalanceText.setText("Sika a na wo wɔ GHS 5000")

        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ############################ NEW BALANCE TEXT ############################
        ##########################################################################
        self.atmui.newbalanceText.setText("Sika a aka GHS 4000")

        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ######################### BACK TO MAIN MENU TEXT #########################
        ##########################################################################
        self.atmui.receiptoptionBtn.setText("WIE")

        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.atmui.successTitle.setText("MO")


        ########################## RECEIPT REQUEST PAGE ##########################
        ############################# NO BUTTON TEXT #############################
        ##########################################################################
        self.atmui.confirmreceiptNoBtn.setText("DAABI")

        ########################## RECEIPT REQUEST PAGE ##########################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.atmui.receiptrequestText.setText("Mepakyɛw wopɛ RECEIPT anaa?")
        
        ########################## RECEIPT REQUEST PAGE ##########################
        ############################ Yes BUTTON TEXT #############################
        ##########################################################################
        self.atmui.confirmreceiptYesBtn.setText("AANE")


        ############################# RECEIPT PAGE ###############################
        ####################### TRANSACTION NUMBER TEXT ##########################
        ##########################################################################
        self.atmui.ReceipttransactionnumberText.setText("Transaction Nɔma: 21324568624")

        ############################# RECEIPT PAGE ###############################
        ########################## ACCOUNT NAME TEXT #############################
        ##########################################################################
        self.atmui.ReceiptaccountnameText.setText("Account Din: ABA")

        ############################# RECEIPT PAGE ###############################
        ######################## WITHDRAWN AMOUNT TEXT ###########################
        ##########################################################################
        self.atmui.ReceiptamountwithdrawnText.setText("Sika a woyii yɛ: GHS 1000")

        ############################# RECEIPT PAGE ###############################
        ########################## NEW BALANCE TEXT ##############################
        ##########################################################################
        self.atmui.ReceiptnewbalanceText2.setText("Sika a aka: GHS 4000")

        ############################# RECEIPT PAGE ###############################
        ############################ THANK YOU TEXT ##############################
        ##########################################################################
        self.atmui.thankyouText.setText("TECH SEALS SIKAKORABIA \nda woase!")

        ############################# RECEIPT PAGE ###############################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.atmui.receiptTitle.setText("RECEIPT")

        ############################# RECEIPT PAGE ###############################
        #################### BACK TO MAIN MENU BUTTON TEXT #######################
        ##########################################################################
        self.atmui.backtoMenuBtn2.setText("WIE")


        ##################### PERFORM NEW TRANSACTION PAGE #######################
        ############################# NO BUTTON TEXT #############################
        ##########################################################################
        self.atmui.newtransactionNoBtn.setText("DAABI")

        ##################### PERFORM NEW TRANSACTION PAGE #######################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.atmui.newtransactionText.setText("Wopɛ sɛ woyɛ biribi foforɔ \nbio?")
        
        ##################### PERFORM NEW TRANSACTION PAGE #######################
        ############################ Yes BUTTON TEXT #############################
        ##########################################################################
        self.atmui.newtransactionYesBtn.setText("AANE")


        ############################ MOMO MENU PAGE ##############################
        ######################## AIRTELTIGO BUTTON TEXT ##########################
        ##########################################################################
        self.atmui.airtelBtn.setText("AIRTELTIGO")

        ############################ MOMO MENU PAGE ##############################
        ########################## VODAFONE BUTTON TEXT ##########################
        ##########################################################################
        self.atmui.vodafoneBtn.setText("VODAFONE")

        ############################ MOMO MENU PAGE ##############################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.atmui.momoText.setText("Wo pɛ Network bɛn?")

        ############################ MOMO MENU PAGE ##############################
        ############################ MTN BUTTON TEXT #############################
        ##########################################################################
        self.atmui.mtnBtn.setText("MTN")

        ############################ MOMO MENU PAGE ##############################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.atmui.momoTitle.setText("MOBILE MONEY")

        ############################ MOMO MENU PAGE ##############################
        ####################### BACK TO MAIN BUTTON TEXT #########################
        ##########################################################################
        self.atmui.mainmenuBtn2.setText("AHYƐASEƐ")

        ######################## TRANSACTION CODE PAGE ###########################
        ##################### CODE INPUT INSTRUCTION TEXT ########################
        ##########################################################################
        self.atmui.transcodeInputTitle.setText("Bɔ CODE no wɔ ha")

        ######################## TRANSACTION CODE PAGE ###########################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.atmui.transactioncodeInput.setPlaceholderText("TRANSACTION CODE")

        ######################## TRANSACTION CODE PAGE ###########################
        ######################### Submit BUTTON TEXT #############################
        ##########################################################################
        self.atmui.transcodeSubmitBtn.setText("MANE")

        ######################## TRANSACTION CODE PAGE ###########################
        ############################# TITLE TEXT #################################
        ##########################################################################
        self.atmui.transactioncodeTitle.setText("TRANSACTION CODE")

        ######################## TRANSACTION CODE PAGE ###########################
        ############################## CODE TEXT #################################
        ##########################################################################
        self.atmui.transactioncodeText.setText("682386")

        ######################## TRANSACTION CODE PAGE ###########################
        ############################# BODY TEXT ##################################
        ##########################################################################
        self.atmui.transcodeParagraph.setText("Yɛ a mane Transaction Code no \nwɔ wo fon no so")
        
        
        ######################### MOMO WITHDRAWAL PAGE ###########################
        ############################# CURRENCY TEXT ##############################
        ##########################################################################
        self.atmui.momocurrencyText.setText("GHS")

        ######################### MOMO WITHDRAWAL PAGE ###########################
        ########################## Submit BUTTON TEXT ############################
        ##########################################################################
        self.atmui.momowithdrawSubmitBtn.setText("MANE")

        ######################### MOMO WITHDRAWAL PAGE ###########################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.atmui.momowithdrawTitle.setText("Bɔ sika dodow a wopɛ")


        ##################### CONFIRM MOMO WITHDRAWAL PAGE #######################
        ########################### NO BUTTON TEXT ###############################
        ##########################################################################
        self.atmui.momoconfirmwithdrawNoBtn.setText("DAABI")

        ##################### CONFIRM MOMO WITHDRAWAL PAGE #######################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.atmui.momoconfirmwithdrawText.setText("Mepakyɛw hwɛ sɛ sika no aso GHS 1000")

        ##################### CONFIRM MOMO WITHDRAWAL PAGE #######################
        ########################### Yes BUTTON TEXT ##############################
        ##########################################################################
        self.atmui.momoconfirmwithdrawYesBtn.setText("AANE")


        ####################### MOMO PIN CONFIRM PAGE ############################
        ############################# PIN TEXT ###################################
        ##########################################################################
        self.atmui.momopinText.setText("9562")

        ####################### MOMO PIN CONFIRM PAGE ############################
        ############################## BODY TEXT #################################
        ##########################################################################
        self.atmui.momopinParagraph.setText("GENERIC MOBILE MONEY PIN")

        ####################### MOMO PIN CONFIRM PAGE ############################
        ############################# TITLE TEXT #################################
        ##########################################################################
        self.atmui.momopinTitle.setText("MOBILE MONEY PIN")

        ####################### MOMO PIN CONFIRM PAGE ############################
        #################### PIN INPUT PLACEHOLDER TEXT ##########################
        ##########################################################################
        self.atmui.momopinInput.setPlaceholderText("BƆ MOMO PIN")

        ####################### MOMO PIN CONFIRM PAGE ############################
        #################### PIN INPUT PLACEHOLDER TEXT ##########################
        ##########################################################################
        self.atmui.momopinSubmitBtn.setText("MANE")

        #################### MOMO WITHDRAW SUCCESS PAGE ##########################
        ################## BACK TO MAIN MENU BUTTON TEXT #########################
        ##########################################################################
        self.atmui.backtoMenuBtn3.setText("WIE")

        #################### MOMO WITHDRAW SUCCESS PAGE ##########################
        ############################ TITLE TEXT ##################################
        ##########################################################################
        self.atmui.momosuccessTitle.setText("MOBILE MONEY")

        #################### MOMO WITHDRAW SUCCESS PAGE ##########################
        ############################ BODY TEXT ###################################
        ##########################################################################
        self.atmui.momosuccessText.setText("Mo! Watumi ayi sika no!")


        ####################### ACCOUNT BALANCE PAGE #############################
        ############################ BODY TEXT ###################################
        ##########################################################################
        self.atmui.balanceText.setText("Wo sika a aka yɛ\n""GHS 3000.00")

        ####################### ACCOUNT BALANCE PAGE #############################
        ############################ BODY TEXT ###################################
        ##########################################################################
        self.atmui.backtoMenuBtn4.setText("WIE")

        ####################### ACCOUNT BALANCE PAGE #############################
        ############################ TITLE TEXT ##################################
        ##########################################################################
        self.atmui.balanceTitle.setText("HWƐ WO SIKA A AKA")


        ######################## CONFIRM LOGOUT PAGE #############################
        ############################ TITLE TEXT ##################################
        ##########################################################################
        self.atmui.confirmquitText.setText("Wopɛ sɛ wogyae?")

        ######################## CONFIRM LOGOUT PAGE #############################
        ########################## Yes BUTTON TEXT ###############################
        ##########################################################################
        self.atmui.confirmquitYesBtn.setText("AANE")

        ######################## CONFIRM LOGOUT PAGE #############################
        ########################### NO BUTTON TEXT ###############################
        ##########################################################################
        self.atmui.confirmquitNoBtn.setText("DAABI")


        self.atmui.main.setCurrentWidget(self.atmui.loginPage)
        self.atmui.loginBtn.clicked.connect(lambda: UIFunctions.loginfunction(self))



