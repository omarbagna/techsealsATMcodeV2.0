import random
import os
from playsound import playsound
from ATMapp import MainWindow


class UIFunctions(MainWindow):
    
    global session, balance, currency, amountWithdrawn, newBalance, transactionCode, momoAmount, momoPin
    
    # USER DETAILS
    def data():
        userArray=[{'username':'aba', 'pin':2121, 'balance':{'GHS':100000, 'USD':80000} },
        {'username':'akosua', 'pin':4000, 'balance':{'GHS':280, 'USD':450} },
        {'username':'eben', 'pin':5461, 'balance':{'GHS':800, 'USD':300} },
        {'username':'bet', 'pin':3197, 'balance':{'GHS':995000, 'USD':980000} },
        {'username':'david', 'pin':3216, 'balance':{'GHS':789, 'USD':250} },
        {'username':'dna', 'pin':1234, 'balance':{'GHS':25000, 'USD':15000} },
        {'username':'dave', 'pin':1034, 'balance':{'GHS':250, 'USD':8000} },
        {'username':'esi', 'pin':7744, 'balance':{'GHS':45000, 'USD':100000} },
        {'username':'esinam', 'pin':1110, 'balance':{'GHS':5000, 'USD':20000} },
        {'username':'emmanuel', 'pin':2145, 'balance':{'GHS':8943, 'USD':2153} },
        {'username':'van', 'pin':2111, 'balance':{'GHS':15000, 'USD':80000} },
        {'username':'bagna', 'pin':7438, 'balance':{'GHS':555000, 'USD':300000} }]
        
        return userArray

# ENGLISH CODE
    def englishCode(self):

        self.atmui.main.setCurrentWidget(self.atmui.loginPage)      
        self.atmui.loginBtn.clicked.connect(lambda: UIFunctions.loginfunction(self))
        self.atmui.cardlessBtn.clicked.connect(lambda: UIFunctions.momo(self))
        

    # USER LOGIN INTERACTION
    def loginfunction(self):
        
        global session, balance

        userName = (self.atmui.usernameInput.text()).lower()
        pin = self.atmui.loginpinInput.text()
        
        def userLogin(userName):

            for userdata in UIFunctions.data():

                sessiondata = {'username':'unknown', 'pin':0000, 'balance':{'GHS':0, 'USD':0} } 

                # Checks for user existence and says a welcome message

                if userName == userdata['username']:
                    sessiondata = userdata #Transfers the found users bank info in to sessiondata variable
                    break  
                    
                else:
                    pass  

            return sessiondata


        def pinVerify(userPin):
    
            #valid = False
            try:
                if userPin == pin:
                   UIFunctions.atmMenu(self)
                   #print('valid')
                    
            except:
                pass
                           
            return 

        # RETRIEVE SPECIFIED USER DETAILS FROM DICTIONARY TO SPECIFIED VARIABLE
        session = userLogin(userName)


        # RETRIEVE SPECIFIED USER PIN AND STORE TO VARIABLE
        userPin = str(session['pin'])

        # RUN PIN VERIFICATION FUNCTION
        pinVerify(userPin)

        # RETRIEVE USER BALANCE
        balance = session['balance']
    
    
    # ATM MENU INTERACTION
    def atmMenu(self):

        self.atmui.main.setCurrentWidget(self.atmui.menuPage)
        self.atmui.welcomeTitle.setText("Welcome "+session['username'].upper())

        self.atmui.balanceBtn.clicked.connect(lambda: UIFunctions.crntBalance(self))
        self.atmui.withdrawalBtn.clicked.connect(lambda: UIFunctions.withdrawUpdate(self))
        self.atmui.momoBtn.clicked.connect(lambda: UIFunctions.momo(self))
        self.atmui.logoutBtn.clicked.connect(lambda: UIFunctions.quitPage(self))


    # CURRENT BALANCE INTERACTION
    def crntBalance(self):
        self.atmui.main.setCurrentWidget(self.atmui.balancePage)

        ghsBalance = balance['GHS']
        usdBalance = balance['USD']

        self.atmui.balanceText.setText("Your current balance is\nGHS "+str(ghsBalance)+"\nUSD "+str(usdBalance))
        self.atmui.backtoMenuBtn4.clicked.connect(lambda: UIFunctions.newTransactions(self))
    

    # WITHDRAWAL INTERACTION
    def withdrawUpdate(self):

        self.atmui.main.setCurrentWidget(self.atmui.withdrawalcurrencyPage)
        self.atmui.cediBtn.clicked.connect(lambda: UIFunctions.ghsClicked(self))
        self.atmui.dollarBtn.clicked.connect(lambda: UIFunctions.usdClicked(self))

    def ghsClicked(self):
        global currency
        currency = 'GHS'
        self.atmui.currencyText.setText(currency)
        UIFunctions.withdrawalAmount(self)

    def usdClicked(self):
        global currency
        currency = 'USD'
        self.atmui.currencyText.setText(currency)
        UIFunctions.withdrawalAmount(self)

    
    def withdrawalAmount(self):
        self.atmui.main.setCurrentWidget(self.atmui.withdrawalamountPage)

        self.atmui.withdrawalSubmitBtn.clicked.connect(lambda: UIFunctions.withdrawFunction(self))


    def withdrawFunction(self):

        global amountWithdrawn
        # SET A MINIMUM BALANCE LIMIT
        minimumBalance = 50

        # SET A MAXIMUM WITHDRAWAL LIMIT
        maxWithdrawal = 5000

        
        amountWithdrawn = int(self.atmui.withdrawalamountInput.text())
        
        # TAKE AMOUNT INPUT
        # CHECK THE AMOUNT VALUE INPUTTED
        try:
        
            # IF THE WITHDRAWAL AMOUNT IS LESS THAN THE USERS BALANCE MOVE TO THE NEXT STEP
            if amountWithdrawn < balance[currency]:
                # CHECK USER BALANCE AFTER SPECIFIED WITHDRAWAL AMOUNT IS WITHDRAWN
                balanceAfterWithdraw = balance[currency] - amountWithdrawn
                
                # CHECK IF BALANCE AFTER WITHDRAWAL IS LESS THAN MINIMUM ALLOWED BALANCE AND ASK USER TO TRY AGAIN
                if balanceAfterWithdraw < minimumBalance:
                   pass

                # CHECK IF WITHDRAWAL AMOUNT IS GREATER THAN MAXIMUM WITHDRAWAL LIMIT AND ASK USER TO TRY AGAIN
                elif amountWithdrawn > maxWithdrawal:
                   pass

                else:
                    UIFunctions.confirmwithdrawFunction(self)
            

        # IF THE USER DOES NOT INPUT WHOLE NUMBERS ASK USER TO TRY AGAIN
        except:
            pass
    
        # HOLD CURRENCY AND AMOUNT SPECIFIED BY USER
        amountWithdrawn


    def confirmwithdrawFunction(self):
        self.atmui.confirmwithdrawalText.setText("Confirm Withdrawal of "+currency+' '+str(amountWithdrawn))
        self.atmui.main.setCurrentWidget(self.atmui.confirmwithdrawalPage)

        self.atmui.confirmwithdrawYesBtn.clicked.connect(lambda: UIFunctions.confirmwithdrawYesclicked(self))
        self.atmui.confirmwithdrawNoBtn.clicked.connect(lambda: UIFunctions.confirmwithdrawNoclicked(self))


    def confirmwithdrawYesclicked(self):
        UIFunctions.successfulWithdrawal(self)
    

    def confirmwithdrawNoclicked(self):
        UIFunctions.newTransactions(self)


    def successfulWithdrawal(self):
        global newBalance
        
        cwd = os.getcwd()
        self.atmui.withdrawnamountText.setText("Successful Withdrawal of "+currency+' '+str(amountWithdrawn))
        self.atmui.previousbalanceText.setText("Previous Balance was "+currency+' '+str(balance[currency]))
        newBalance = balance[currency] - amountWithdrawn
        self.atmui.newbalanceText.setText("New Balance is "+currency+' '+str(newBalance))
        
        playsound(r"{0}\ATM_soundEffect4.mp3".format(cwd))
        self.atmui.main.setCurrentWidget(self.atmui.successfulwithdrawalPage)
        self.atmui.receiptoptionBtn.clicked.connect(lambda: UIFunctions.receiptoptionFunction(self))


    # RECEIPT OPTION FUNCTIONALITY
    def receiptYesclicked(self):
        UIFunctions.receiptFunction(self)


    def receiptNoclicked(self):
        UIFunctions.newTransactions(self)


    def receiptoptionFunction(self):
        balance[currency] = newBalance
        self.atmui.main.setCurrentWidget(self.atmui.receiptrequestPage)
        self.atmui.confirmreceiptYesBtn.clicked.connect(lambda: UIFunctions.receiptYesclicked(self))
        self.atmui.confirmreceiptNoBtn.clicked.connect(lambda: UIFunctions.receiptNoclicked(self))


    def receiptFunction(self):

        self.atmui.ReceipttransactionnumberText.setText('Transaction Number: '+str(random.randint(100000000000,999999999999)))
        self.atmui.ReceiptaccountnameText.setText(str("Account Name: "+session['username'].upper()))
        self.atmui.ReceiptamountwithdrawnText.setText("Amount Withdrawn: "+currency+' '+str(amountWithdrawn))      
        self.atmui.ReceiptnewbalanceText2.setText("New Available Balance: "+currency+' '+str(newBalance))
        self.atmui.main.setCurrentWidget(self.atmui.receiptPage)
        self.atmui.backtoMenuBtn2.clicked.connect(lambda: UIFunctions.newTransactions(self))



    # MOBILE MONEY PAGE INTERACTION
    def momo(self):
        self.atmui.main.setCurrentWidget(self.atmui.momomenuPage)

        self.atmui.mainmenuBtn2.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.menuPage))

        self.atmui.mtnBtn.clicked.connect(lambda: UIFunctions.transactioncodeFunction(self))
        self.atmui.vodafoneBtn.clicked.connect(lambda: UIFunctions.transactioncodeFunction(self))
        self.atmui.airtelBtn.clicked.connect(lambda: UIFunctions.transactioncodeFunction(self))


    def transactioncodeFunction(self):
        global transactionCode

        transactionCode = random.randint(100000,999999)
        self.atmui.transactioncodeText.setText(str(transactionCode))
        self.atmui.main.setCurrentWidget(self.atmui.transactioncodePage)
        self.atmui.transcodeSubmitBtn.clicked.connect(lambda: UIFunctions.transactioncodeVerify(self))


    def transactioncodeVerify(self):

        try: 
            transactionCodeInput = int(self.atmui.transactioncodeInput.text())
            if transactionCode == transactionCodeInput:
                UIFunctions.momowithdrawFunction(self)
            else:
                print('Wrong Code try again')
                UIFunctions.transactioncodeFunction(self)
                pass

        except:
            pass


    def momowithdrawFunction(self):
        self.atmui.main.setCurrentWidget(self.atmui.momowithdrawPage)
        self.atmui.momowithdrawSubmitBtn.clicked.connect(lambda: UIFunctions.momowithdrawAmount(self))


    def momowithdrawAmount(self):

        global momoAmount
        
        try:
            momoAmount = int(self.atmui.momowithdrawamountInput.text())

            if momoAmount <= 2000:
                UIFunctions.confirmmomoFunction(self)
                

            elif momoAmount > 2000:  
                print ("Unsuccessful. You cannot withdraw more than GHS 2000")
                UIFunctions.momowithdrawFunction(self)
                pass

        except:
            print ('Invalid input. Please enter a number')
            pass


    def confirmmomoYesclicked(self):
        UIFunctions.momopinFunction(self)


    def confirmmomoNoclicked(self):
        UIFunctions.newTransactions(self)


    def confirmmomoFunction(self):
        self.atmui.momoconfirmwithdrawalText.setText("Confirm Withdrawal of GHS "+str(momoAmount))
        self.atmui.main.setCurrentWidget(self.atmui.momoconfirmPage)
        self.atmui.momoconfirmwithdrawYesBtn.clicked.connect(lambda: UIFunctions.confirmmomoYesclicked(self))
        self.atmui.momoconfirmwithdrawNoBtn.clicked.connect(lambda: UIFunctions.confirmmomoNoclicked(self))
        
    
    def momopinFunction(self):
        global momoPin

        momoPin = random.randint(1000,9999)
        self.atmui.momopinText.setText(str(momoPin))
        self.atmui.main.setCurrentWidget(self.atmui.momopinPage)
        self.atmui.momopinSubmitBtn.clicked.connect(lambda: UIFunctions.momopinVerify(self))
        

    def momopinVerify(self):

        try:
            momoPinValid = int(self.atmui.momopinInput.text())
            
            if momoPinValid == momoPin:
                UIFunctions.momosuccessFunction(self)

            elif momoPinValid != momoPin:
                UIFunctions.momopinFunction(self)
                pass

        except:
            pass


    def momosuccessFunction(self):
        cwd = os.getcwd()
        playsound(r"{0}\ATM_soundEffect4.mp3".format(cwd))
        self.atmui.main.setCurrentWidget(self.atmui.momosuccessPage)
        self.atmui.backtoMenuBtn3.clicked.connect(lambda: UIFunctions.newTransactions(self))



    # NEW TRANSACTION PAGE INTERACTION
    def newTransactions(self):
        self.atmui.main.setCurrentWidget(self.atmui.newtransactionPage)

        self.atmui.newtransactionYesBtn.clicked.connect(lambda: UIFunctions.newTransactionYes(self))
        self.atmui.newtransactionNoBtn.clicked.connect(lambda: UIFunctions.newTransactionNo(self))

    def newTransactionYes(self):
        UIFunctions.atmMenu(self)

    def newTransactionNo(self):
        UIFunctions.quitPage(self)


    # QUIT PAGE INTERACTION
    def quitPage(self):
        self.atmui.main.setCurrentWidget(self.atmui.confirmquitPage)

        self.atmui.confirmquitYesBtn.clicked.connect(lambda: UIFunctions.confirmquitYes(self))
        self.atmui.confirmquitNoBtn.clicked.connect(lambda: UIFunctions.confirmquitNo(self))
    
    def confirmquitYes(self):
        self.atmui.main.setCurrentWidget(self.atmui.exitPage)

    def confirmquitNo(self):
        UIFunctions.atmMenu(self)


# TWI CODE
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
        self.atmui.welcomeTitle.setText("Akwaaba ")

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

        ######################## CASH WAIT PAGE #########################
        ############################# BODY TEXT #############################
        ##########################################################################
        self.atmui.cashwaitText.setText("MEPAKYƐW TWƐN \n""SIKA NO BƐBA SEESIA")


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
        self.atmui.momoconfirmwithdrawalText.setText("Mepakyɛw hwɛ sɛ sika no aso GHS 1000")

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
        self.atmui.loginBtn.clicked.connect(lambda: UIFunctions.loginfunctionTwi(self))
        self.atmui.cardlessBtn.clicked.connect(lambda: UIFunctions.momoTwi(self))


    # USER LOGIN INTERACTION TWI
    def loginfunctionTwi(self):
        global session, balance
    
        userName = (self.atmui.usernameInput.text()).lower()
        pin = self.atmui.loginpinInput.text()
        
        def userLogin(userName):

            for userdata in UIFunctions.data():

                sessiondata = {'username':'unknown', 'pin':0000, 'balance':{'GHS':0, 'USD':0} } 


                if userName == userdata['username']:
                    sessiondata = userdata #Transfers the found users bank info in to sessiondata variable
                    break  
                    
                else:
                    pass  

            return sessiondata


        def pinVerify(userPin):

            try:
                if userPin == pin :
                    UIFunctions.atmMenuTwi(self)
                    
            except:
                pass
                            
            return 

        # RETRIEVE SPECIFIED USER DETAILS FROM DICTIONARY TO SPECIFIED VARIABLE
        session = userLogin(userName)


        # RETRIEVE SPECIFIED USER PIN AND STORE TO VARIABLE
        userPin = str(session['pin'])

        # RUN PIN VERIFICATION FUNCTION
        pinVerify(userPin)

        # RETRIEVE USER BALANCE
        balance = session['balance']


    # ATM MENU INTERACTION TWI
    def atmMenuTwi(self):

        # DISPLAY ATM MENU
        self.atmui.main.setCurrentWidget(self.atmui.menuPage)
        self.atmui.welcomeTitle.setText("Akwaaba "+session['username'].upper())

        self.atmui.balanceBtn.clicked.connect(lambda: UIFunctions.crntBalanceTwi(self))
        self.atmui.withdrawalBtn.clicked.connect(lambda: UIFunctions.withdrawUpdateTwi(self))
        self.atmui.momoBtn.clicked.connect(lambda: UIFunctions.momoTwi(self))
        self.atmui.logoutBtn.clicked.connect(lambda: UIFunctions.quitPage(self))


    # CURRENT BALANCE INTERACTION TWI
    def crntBalanceTwi(self):
        self.atmui.main.setCurrentWidget(self.atmui.balancePage)

        ghsBalance = balance['GHS']
        usdBalance = balance['USD']

        self.atmui.balanceText.setText("Wo sika a aka yɛ\nGHS "+str(ghsBalance)+"\nUSD "+str(usdBalance))
        self.atmui.backtoMenuBtn4.clicked.connect(lambda: UIFunctions.newTransactionsTwi(self))


    # WITHDRAWAL INTERACTION TWI
    def withdrawUpdateTwi(self):

        self.atmui.main.setCurrentWidget(self.atmui.withdrawalcurrencyPage)
        self.atmui.cediBtn.clicked.connect(lambda: UIFunctions.ghsClickedTwi(self))
        self.atmui.dollarBtn.clicked.connect(lambda: UIFunctions.usdClickedTwi(self))

    def ghsClickedTwi(self):
        global currency
        currency = 'GHS'
        self.atmui.currencyText.setText(currency)
        UIFunctions.withdrawalAmountTwi(self)

    def usdClickedTwi(self):
        global currency
        currency = 'USD'
        self.atmui.currencyText.setText(currency)
        UIFunctions.withdrawalAmountTwi(self)

    
    def withdrawalAmountTwi(self):
        self.atmui.main.setCurrentWidget(self.atmui.withdrawalamountPage)

        self.atmui.withdrawalSubmitBtn.clicked.connect(lambda: UIFunctions.withdrawFunctionTwi(self))


    def withdrawFunctionTwi(self):

        global amountWithdrawn
        # SET A MINIMUM BALANCE LIMIT
        minimumBalance = 50

        # SET A MAXIMUM WITHDRAWAL LIMIT
        maxWithdrawal = 5000

        
        amountWithdrawn = int(self.atmui.withdrawalamountInput.text())
        
        # TAKE AMOUNT INPUT
        # CHECK THE AMOUNT VALUE INPUTTED
        try:
        
            # IF THE WITHDRAWAL AMOUNT IS LESS THAN THE USERS BALANCE MOVE TO THE NEXT STEP
            if amountWithdrawn < balance[currency]:
                # CHECK USER BALANCE AFTER SPECIFIED WITHDRAWAL AMOUNT IS WITHDRAWN
                balanceAfterWithdraw = balance[currency] - amountWithdrawn
                
                # CHECK IF BALANCE AFTER WITHDRAWAL IS LESS THAN MINIMUM ALLOWED BALANCE AND ASK USER TO TRY AGAIN
                if balanceAfterWithdraw < minimumBalance:
                   pass

                # CHECK IF WITHDRAWAL AMOUNT IS GREATER THAN MAXIMUM WITHDRAWAL LIMIT AND ASK USER TO TRY AGAIN
                elif amountWithdrawn > maxWithdrawal:
                   pass

                else:
                    UIFunctions.confirmwithdrawFunctionTwi(self)
            

        # IF THE USER DOES NOT INPUT WHOLE NUMBERS ASK USER TO TRY AGAIN
        except:
            pass
    
        # HOLD CURRENCY AND AMOUNT SPECIFIED BY USER
        amountWithdrawn



    def confirmwithdrawFunctionTwi(self):
        self.atmui.confirmwithdrawalText.setText("Mepakyɛw hwɛ sɛ sika no aso "+currency+' '+str(amountWithdrawn))
        self.atmui.main.setCurrentWidget(self.atmui.confirmwithdrawalPage)

        self.atmui.confirmwithdrawYesBtn.clicked.connect(lambda: UIFunctions.confirmwithdrawYesclickedTwi(self))
        self.atmui.confirmwithdrawNoBtn.clicked.connect(lambda: UIFunctions.confirmwithdrawNoclickedTwi(self))

    def confirmwithdrawYesclickedTwi(self):
        UIFunctions.successfulWithdrawalTwi(self)
    

    def confirmwithdrawNoclickedTwi(self):
        UIFunctions.newTransactionsTwi(self)


    def successfulWithdrawalTwi(self):
        global newBalance

        cwd = os.getcwd()
        self.atmui.withdrawnamountText.setText("Watumi ayi "+currency+' '+str(amountWithdrawn))
        self.atmui.previousbalanceText.setText("Sika a na wo wɔ "+currency+' '+str(balance[currency]))
        newBalance = balance[currency] - amountWithdrawn
        self.atmui.newbalanceText.setText("Sika a aka "+currency+' '+str(newBalance))
        
        playsound(r"{0}\ATM_soundEffect4.mp3".format(cwd))
        self.atmui.main.setCurrentWidget(self.atmui.successfulwithdrawalPage)
        self.atmui.receiptoptionBtn.clicked.connect(lambda: UIFunctions.receiptoptionFunctionTwi(self))


    # RECEIPT OPTION FUNCTIONALITY
    def receiptYesclickedTwi(self):
        UIFunctions.receiptFunctionTwi(self)


    def receiptNoclickedTwi(self):
        UIFunctions.newTransactionsTwi(self)


    def receiptoptionFunctionTwi(self):
        balance[currency] = newBalance
        self.atmui.main.setCurrentWidget(self.atmui.receiptrequestPage)
        self.atmui.confirmreceiptYesBtn.clicked.connect(lambda: UIFunctions.receiptYesclickedTwi(self))
        self.atmui.confirmreceiptNoBtn.clicked.connect(lambda: UIFunctions.receiptNoclickedTwi(self))


    def receiptFunctionTwi(self):

        self.atmui.ReceipttransactionnumberText.setText('Transaction Nɔma: '+str(random.randint(100000000000,999999999999)))
        self.atmui.ReceiptaccountnameText.setText(str("Account Din: "+session['username'].upper()))
        self.atmui.ReceiptamountwithdrawnText.setText("Sika a woyii yɛ: "+currency+' '+str(amountWithdrawn))      
        self.atmui.ReceiptnewbalanceText2.setText("Sika a aka: "+currency+' '+str(newBalance))
        self.atmui.main.setCurrentWidget(self.atmui.receiptPage)
        self.atmui.backtoMenuBtn2.clicked.connect(lambda: UIFunctions.newTransactionsTwi(self))


    # MOBILE MONEY PAGE INTERACTION TWI
    def momoTwi(self):
        self.atmui.main.setCurrentWidget(self.atmui.momomenuPage)

        self.atmui.mainmenuBtn2.clicked.connect(lambda: self.atmui.main.setCurrentWidget(self.atmui.menuPage))

        self.atmui.mtnBtn.clicked.connect(lambda: UIFunctions.transactioncodeFunctionTwi(self))
        self.atmui.vodafoneBtn.clicked.connect(lambda: UIFunctions.transactioncodeFunctionTwi(self))
        self.atmui.airtelBtn.clicked.connect(lambda: UIFunctions.transactioncodeFunctionTwi(self))


    def transactioncodeFunctionTwi(self):
        global transactionCode

        transactionCode = random.randint(100000,999999)
        self.atmui.transactioncodeText.setText(str(transactionCode))
        self.atmui.main.setCurrentWidget(self.atmui.transactioncodePage)
        self.atmui.transcodeSubmitBtn.clicked.connect(lambda: UIFunctions.transactioncodeVerifyTwi(self))


    def transactioncodeVerifyTwi(self):

        try: 
            transactionCodeInput = int(self.atmui.transactioncodeInput.text())
            if transactionCode == transactionCodeInput:
                UIFunctions.momowithdrawFunctionTwi(self)
            else:
                print('Wrong Code try again')
                UIFunctions.transactioncodeFunctionTwi(self)
                pass

        except:
            pass


    def momowithdrawFunctionTwi(self):
        self.atmui.main.setCurrentWidget(self.atmui.momowithdrawPage)
        self.atmui.momowithdrawSubmitBtn.clicked.connect(lambda: UIFunctions.momowithdrawAmountTwi(self))


    def momowithdrawAmountTwi(self):

        global momoAmount
        
        try:
            momoAmount = int(self.atmui.momowithdrawamountInput.text())

            if momoAmount <= 2000:
                UIFunctions.confirmmomoFunctionTwi(self)
                

            elif momoAmount > 2000:  
                print ("Unsuccessful. You cannot withdraw more than GHS 2000")
                UIFunctions.momowithdrawFunctionTwi(self)
                pass

        except:
            print ('Invalid input. Please enter a number')
            pass


    def confirmmomoYesclickedTwi(self):
        UIFunctions.momopinFunctionTwi(self)


    def confirmmomoNoclickedTwi(self):
        UIFunctions.newTransactionsTwi(self)


    def confirmmomoFunctionTwi(self):
        self.atmui.momoconfirmwithdrawalText.setText("Mepakyɛw hwɛ sɛ sika no aso GHS "+str(momoAmount))
        self.atmui.main.setCurrentWidget(self.atmui.momoconfirmPage)
        self.atmui.momoconfirmwithdrawYesBtn.clicked.connect(lambda: UIFunctions.confirmmomoYesclickedTwi(self))
        self.atmui.momoconfirmwithdrawNoBtn.clicked.connect(lambda: UIFunctions.confirmmomoNoclickedTwi(self))
        
    
    def momopinFunctionTwi(self):
        global momoPin

        momoPin = random.randint(1000,9999)
        self.atmui.momopinText.setText(str(momoPin))
        self.atmui.main.setCurrentWidget(self.atmui.momopinPage)
        self.atmui.momopinSubmitBtn.clicked.connect(lambda: UIFunctions.momopinVerifyTwi(self))
        

    def momopinVerifyTwi(self):

        try:
            momoPinValid = int(self.atmui.momopinInput.text())
            
            if momoPinValid == momoPin:
                UIFunctions.momosuccessFunctionTwi(self)

            elif momoPinValid != momoPin:
                UIFunctions.momopinFunctionTwi(self)
                pass

        except:
            pass


    def momosuccessFunctionTwi(self):
        cwd = os.getcwd()
        playsound(r"{0}\ATM_soundEffect4.mp3".format(cwd))
        self.atmui.main.setCurrentWidget(self.atmui.momosuccessPage)
        self.atmui.backtoMenuBtn3.clicked.connect(lambda: UIFunctions.newTransactionsTwi(self))



    # NEW TRANSACTION PAGE INTERACTION TWI
    def newTransactionsTwi(self):
        self.atmui.main.setCurrentWidget(self.atmui.newtransactionPage)

        self.atmui.newtransactionYesBtn.clicked.connect(lambda: UIFunctions.newTransactionYesTwi(self))
        self.atmui.newtransactionNoBtn.clicked.connect(lambda: UIFunctions.newTransactionNoTwi(self))

    def newTransactionYesTwi(self):
        UIFunctions.atmMenuTwi(self)

    def newTransactionNoTwi(self):
        UIFunctions.quitPage(self)


    # QUIT PAGE INTERACTION TWI
    def quitPage(self):
        self.atmui.main.setCurrentWidget(self.atmui.confirmquitPage)

        self.atmui.confirmquitYesBtn.clicked.connect(lambda: UIFunctions.confirmquitYesTwi(self))
        self.atmui.confirmquitNoBtn.clicked.connect(lambda: UIFunctions.confirmquitNoTwi(self))
    
    def confirmquitYesTwi(self):
        self.atmui.main.setCurrentWidget(self.atmui.exitPage)

    def confirmquitNoTwi(self):
        UIFunctions.atmMenuTwi(self)