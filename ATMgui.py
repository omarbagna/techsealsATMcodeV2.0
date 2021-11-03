
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TechSealsATM(object):
    def setupUi(self, TechSealsATM):
        TechSealsATM.setObjectName("TechSealsATM")
        TechSealsATM.resize(1100, 615)
        TechSealsATM.setMinimumSize(QtCore.QSize(1100, 615))
        TechSealsATM.setMaximumSize(QtCore.QSize(1100, 615))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        TechSealsATM.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/guiImages/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TechSealsATM.setWindowIcon(icon)
        self.body = QtWidgets.QWidget(TechSealsATM)
        self.body.setObjectName("body")
        
        self.main = QtWidgets.QStackedWidget(self.body)
        self.main.setGeometry(QtCore.QRect(0, 0, 1100, 615))
        self.main.setMinimumSize(QtCore.QSize(1100, 615))
        self.main.setMaximumSize(QtCore.QSize(1100, 615))
        self.main.setStyleSheet("QLabel {\n""    color: #fff;\n""    font-family: Open Sans;\n""    font-weight: bold;\n""    font-size: 80px;\n""}\n""\n""QPushButton {\n""    color: #fff;\n""    font-family: Open Sans;\n""    font-size: 35px;\n""    border: none;\n""    border-radius: 10px;\n""    background-color:  rgba(11, 11, 11, 200);\n""}\n""\n""QPushButton:hover {\n""    background-color:  rgba(11, 11, 11, 255);\n""}\n""\n""QPushButton:pressed {\n""    background-color: rgba(11, 11, 11, 230);\n""}\n""\n""QLineEdit {\n""    background: rgba(0, 0, 0, 130);\n""    color: #fff;\n""    font-size: 18px;\n""    padding: 20px;\n""    border: none;\n""    border-radius: 25px;\n""}\n""\n""QStackedWidget::setCurrentIndex/Widget(1)\n""")
        self.main.setObjectName("main")


        ##########################################################################
        #### WELCOME PAGE
        ##########################################################################

        self.welcomePage = QtWidgets.QWidget()
        self.welcomePage.setStyleSheet("#welcomePage {\n""    background-image: url(:/assets/guiImages/welcomeBG.png);\n""}")

        self.welcomePage.setObjectName("welcomePage")
        self.startBtn = QtWidgets.QPushButton(self.welcomePage)
        self.startBtn.setGeometry(QtCore.QRect(440, 450, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(1)
        font.setBold(False)
        font.setWeight(50)
        self.startBtn.setFont(font)
        self.startBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startBtn.setStyleSheet("#startBtn {\n""    background-color: #7ed957;\n""    color: #fff;\n""    border: none;\n""    border-radius: 20px;\n""}\n""\n""#startBtn:hover {\n""    background-color: #9df179;\n""}\n""\n""#startBtn:pressed {\n""    background-color: #76c454;\n""}")

        self.startBtn.setObjectName("startBtn")
        self.main.addWidget(self.welcomePage)


        ##########################################################################
        #### LANGUAGE SELECTOR PAGE
        ##########################################################################
        self.languagePage = QtWidgets.QWidget()
        self.languagePage.setMinimumSize(QtCore.QSize(1100, 615))
        self.languagePage.setMaximumSize(QtCore.QSize(1100, 615))
        self.languagePage.setStyleSheet("#languagePage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.languagePage.setObjectName("languagePage")
        self.pageHead = QtWidgets.QLabel(self.languagePage)
        self.pageHead.setGeometry(QtCore.QRect(0, 160, 1101, 131))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.pageHead.setFont(font)
        self.pageHead.setStyleSheet("background: none;")
        self.pageHead.setAlignment(QtCore.Qt.AlignCenter)
        self.pageHead.setObjectName("pageHead")
        self.englishBtn = QtWidgets.QPushButton(self.languagePage)
        self.englishBtn.setGeometry(QtCore.QRect(240, 340, 251, 71))
        self.englishBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.englishBtn.setObjectName("englishBtn")
        self.twiBtn = QtWidgets.QPushButton(self.languagePage)
        self.twiBtn.setGeometry(QtCore.QRect(570, 340, 251, 71))
        self.twiBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.twiBtn.setObjectName("twiBtn")
        self.main.addWidget(self.languagePage)
        
        
        ##########################################################################
        #### LOGIN PAGE
        ##########################################################################
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setMinimumSize(QtCore.QSize(1100, 615))
        self.loginPage.setMaximumSize(QtCore.QSize(1100, 615))
        self.loginPage.setStyleSheet("#loginPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.loginPage.setObjectName("loginPage")
        self.loginBtn = QtWidgets.QPushButton(self.loginPage)
        self.loginBtn.setGeometry(QtCore.QRect(190, 470, 211, 61))
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setObjectName("loginBtn")
        self.cardlessBtn = QtWidgets.QPushButton(self.loginPage)
        self.cardlessBtn.setGeometry(QtCore.QRect(650, 300, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.cardlessBtn.setFont(font)
        self.cardlessBtn.setStyleSheet("#cardlessBtn {\n""    background-color: rgba(11, 11, 11, 200);\n""}\n""\n""#cardlessBtn:hover {\n""    background-color: rgba(11, 11, 11, 255);\n""}\n""\n""#cardlessBtn:pressed {\n""    background-color: rgba(11, 11, 11, 230);\n""}")

        self.cardlessBtn.setObjectName("cardlessBtn")
        self.line = QtWidgets.QFrame(self.loginPage)
        self.line.setGeometry(QtCore.QRect(550, 210, 31, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setStyleSheet("background: none;\n""color: #fff;")

        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.loginTitle = QtWidgets.QLabel(self.loginPage)
        self.loginTitle.setGeometry(QtCore.QRect(0, 100, 1101, 101))
        self.loginTitle.setStyleSheet("background: none;")
        self.loginTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.loginTitle.setObjectName("loginTitle")
        self.usernameInput = QtWidgets.QLineEdit(self.loginPage)
        self.usernameInput.setGeometry(QtCore.QRect(120, 230, 351, 71))
        self.usernameInput.setInputMask("")
        self.usernameInput.setText("")
        self.usernameInput.setObjectName("usernameInput")
        self.loginpinInput = QtWidgets.QLineEdit(self.loginPage)
        self.loginpinInput.setGeometry(QtCore.QRect(120, 350, 351, 71))
        self.loginpinInput.setStyleSheet("color: grey;")
        self.loginpinInput.setInputMask("")
        self.loginpinInput.setMaxLength(4)
        self.loginpinInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginpinInput.setObjectName("loginpinInput")
        self.main.addWidget(self.loginPage)


        ##########################################################################
        #### FORGOT PIN PAGE
        ##########################################################################
        self.forgotpinPage = QtWidgets.QWidget()
        self.forgotpinPage.setStyleSheet("#forgotpinPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.forgotpinPage.setObjectName("forgotpinPage")
        self.forgotpinTitle = QtWidgets.QLabel(self.forgotpinPage)
        self.forgotpinTitle.setGeometry(QtCore.QRect(0, 130, 1101, 71))
        self.forgotpinTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.forgotpinTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.forgotpinTitle.setObjectName("forgotpinTitle")
        self.frame = QtWidgets.QFrame(self.forgotpinPage)
        self.frame.setGeometry(QtCore.QRect(140, 240, 771, 291))
        self.frame.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.fpNoBtn = QtWidgets.QPushButton(self.frame)
        self.fpNoBtn.setGeometry(QtCore.QRect(430, 150, 131, 61))
        self.fpNoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fpNoBtn.setStyleSheet("#fpNoBtn {\n""    background-color: #ff1616;\n""}\n""\n""#fpNoBtn:hover {\n""    background-color: #f13c3c;\n""}\n""\n""#fpNoBtn:pressed {\n""    background-color: #c20707;\n""}")

        self.fpNoBtn.setFlat(False)
        self.fpNoBtn.setObjectName("fpNoBtn")
        self.fpYesBtn = QtWidgets.QPushButton(self.frame)
        self.fpYesBtn.setGeometry(QtCore.QRect(190, 150, 131, 61))
        self.fpYesBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fpYesBtn.setStyleSheet("#fpYesBtn {\n""    background-color: #7ed957;\n""}\n""\n""#fpYesBtn:hover {\n""    background-color: #9df179;\n""}\n""\n""#fpYesBtn:pressed {\n""    background-color: #76c454;\n""}")

        self.fpYesBtn.setObjectName("fpYesBtn")
        self.forgotpinText = QtWidgets.QLabel(self.frame)
        self.forgotpinText.setGeometry(QtCore.QRect(10, 30, 751, 81))
        self.forgotpinText.setStyleSheet("font-size: 40px;\n""font-weight: normal;\n""background: none;")

        self.forgotpinText.setAlignment(QtCore.Qt.AlignCenter)
        self.forgotpinText.setObjectName("forgotpinText")
        self.main.addWidget(self.forgotpinPage)


        ##########################################################################
        #### VERIFICATION CODE PAGE
        ##########################################################################
        self.verificationcodePage = QtWidgets.QWidget()
        self.verificationcodePage.setStyleSheet("#verificationcodePage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.verificationcodePage.setObjectName("verificationcodePage")
        self.verificationcodeTitle = QtWidgets.QLabel(self.verificationcodePage)
        self.verificationcodeTitle.setGeometry(QtCore.QRect(0, 110, 1101, 91))
        self.verificationcodeTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.verificationcodeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.verificationcodeTitle.setObjectName("verificationcodeTitle")
        self.frame_2 = QtWidgets.QFrame(self.verificationcodePage)
        self.frame_2.setGeometry(QtCore.QRect(120, 280, 411, 241))
        self.frame_2.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verificationcodeText = QtWidgets.QLabel(self.frame_2)
        self.verificationcodeText.setGeometry(QtCore.QRect(10, 120, 391, 61))
        self.verificationcodeText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.verificationcodeText.setAlignment(QtCore.Qt.AlignCenter)
        self.verificationcodeText.setObjectName("verificationcodeText")
        self.vericodeParagraph = QtWidgets.QLabel(self.frame_2)
        self.vericodeParagraph.setGeometry(QtCore.QRect(10, 20, 391, 81))
        self.vericodeParagraph.setStyleSheet("background: none;\n""font-size: 25px;\n""font-weight: normal;")
        
        self.vericodeParagraph.setAlignment(QtCore.Qt.AlignCenter)
        self.vericodeParagraph.setObjectName("vericodeParagraph")
        self.frame_3 = QtWidgets.QFrame(self.verificationcodePage)
        self.frame_3.setGeometry(QtCore.QRect(629, 249, 341, 301))
        self.frame_3.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;\n""\n""")

        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.vericodeInputTitle = QtWidgets.QLabel(self.frame_3)
        self.vericodeInputTitle.setGeometry(QtCore.QRect(10, 40, 321, 41))
        self.vericodeInputTitle.setStyleSheet("background: none;\n""font-size: 30px;")

        self.vericodeInputTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.vericodeInputTitle.setObjectName("vericodeInputTitle")
        self.verificationcodeInput = QtWidgets.QLineEdit(self.frame_3)
        self.verificationcodeInput.setGeometry(QtCore.QRect(40, 110, 261, 61))
        self.verificationcodeInput.setMaxLength(6)
        self.verificationcodeInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verificationcodeInput.setAlignment(QtCore.Qt.AlignCenter)
        self.verificationcodeInput.setObjectName("verificationcodeInput")
        self.vericodeSubmitBtn = QtWidgets.QPushButton(self.frame_3)
        self.vericodeSubmitBtn.setGeometry(QtCore.QRect(110, 200, 131, 51))
        self.vericodeSubmitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vericodeSubmitBtn.setStyleSheet("#vericodeSubmitBtn {\n""    background: rgba(0, 0, 0, 200);\n""    border-radius: 10px;\n""    font-size: 25px;\n""}\n""")

        self.vericodeSubmitBtn.setObjectName("vericodeSubmitBtn")
        self.line_2 = QtWidgets.QFrame(self.verificationcodePage)
        self.line_2.setGeometry(QtCore.QRect(550, 230, 20, 341))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.main.addWidget(self.verificationcodePage)


        ##########################################################################
        #### PIN RESET PAGE
        ##########################################################################
        self.pinchangePage = QtWidgets.QWidget()
        self.pinchangePage.setStyleSheet("#pinchangePage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.pinchangePage.setObjectName("pinchangePage")
        self.pinchangeTitle = QtWidgets.QLabel(self.pinchangePage)
        self.pinchangeTitle.setGeometry(QtCore.QRect(0, 120, 1101, 61))
        self.pinchangeTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.pinchangeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.pinchangeTitle.setObjectName("pinchangeTitle")
        self.frame_4 = QtWidgets.QFrame(self.pinchangePage)
        self.frame_4.setGeometry(QtCore.QRect(340, 210, 421, 351))
        self.frame_4.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;\n""")

        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pinchangeConfirmBtn = QtWidgets.QPushButton(self.frame_4)
        self.pinchangeConfirmBtn.setGeometry(QtCore.QRect(130, 260, 161, 51))
        self.pinchangeConfirmBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pinchangeConfirmBtn.setStyleSheet("#pinchangeConfirmBtn {\n""    background: rgba(0, 0, 0, 200);\n""    border-radius: 10px;\n""    font-size: 25px;\n""}\n""")

        self.pinchangeConfirmBtn.setObjectName("pinchangeConfirmBtn")
        self.newpinInput = QtWidgets.QLineEdit(self.frame_4)
        self.newpinInput.setGeometry(QtCore.QRect(90, 60, 241, 61))
        self.newpinInput.setMaxLength(4)
        self.newpinInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpinInput.setAlignment(QtCore.Qt.AlignCenter)
        self.newpinInput.setObjectName("newpinInput")
        self.newpinconfirmInput = QtWidgets.QLineEdit(self.frame_4)
        self.newpinconfirmInput.setGeometry(QtCore.QRect(90, 160, 241, 61))
        self.newpinconfirmInput.setMaxLength(4)
        self.newpinconfirmInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpinconfirmInput.setAlignment(QtCore.Qt.AlignCenter)
        self.newpinconfirmInput.setObjectName("newpinconfirmInput")
        self.main.addWidget(self.pinchangePage)


        ##########################################################################
        #### MAIN MENU PAGE
        ##########################################################################
        self.menuPage = QtWidgets.QWidget()
        self.menuPage.setStyleSheet("#menuPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.menuPage.setObjectName("menuPage")
        self.welcomeTitle = QtWidgets.QLabel(self.menuPage)
        self.welcomeTitle.setGeometry(QtCore.QRect(10, 130, 1071, 131))
        self.welcomeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeTitle.setObjectName("welcomeTitle")
        self.welcomeText = QtWidgets.QLabel(self.menuPage)
        self.welcomeText.setGeometry(QtCore.QRect(10, 270, 1071, 71))
        self.welcomeText.setStyleSheet("background: none;\n""font-size: 30px;")

        self.welcomeText.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeText.setObjectName("welcomeText")
        self.balanceBtn = QtWidgets.QPushButton(self.menuPage)
        self.balanceBtn.setGeometry(QtCore.QRect(40, 410, 291, 81))
        self.balanceBtn.setObjectName("balanceBtn")
        self.withdrawalBtn = QtWidgets.QPushButton(self.menuPage)
        self.withdrawalBtn.setGeometry(QtCore.QRect(400, 410, 291, 81))
        self.withdrawalBtn.setObjectName("withdrawalBtn")
        self.momoBtn = QtWidgets.QPushButton(self.menuPage)
        self.momoBtn.setGeometry(QtCore.QRect(770, 410, 291, 81))
        self.momoBtn.setObjectName("momoBtn")
        self.logoutBtn = QtWidgets.QPushButton(self.menuPage)
        self.logoutBtn.setGeometry(QtCore.QRect(880, 30, 181, 61))
        self.logoutBtn.setStyleSheet("#logoutBtn {\n""    background-color: #ff1616;\n""    font-weight: bold;\n""    font-size: 25px;\n""}\n""\n""#logoutBtn:hover {\n""    background-color: #f13c3c;\n""}\n""\n""#logoutBtn:pressed {\n""    background-color: #c20707;\n""}")

        self.logoutBtn.setObjectName("logoutBtn")
        self.main.addWidget(self.menuPage)


        ##########################################################################
        #### WITHDRAWAL CURRENCY PAGE
        ##########################################################################
        self.withdrawalcurrencyPage = QtWidgets.QWidget()
        self.withdrawalcurrencyPage.setStyleSheet("#withdrawalcurrencyPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.withdrawalcurrencyPage.setObjectName("withdrawalcurrencyPage")
        self.withdrawalcurrencyTitle = QtWidgets.QLabel(self.withdrawalcurrencyPage)
        self.withdrawalcurrencyTitle.setGeometry(QtCore.QRect(0, 120, 1101, 71))
        self.withdrawalcurrencyTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.withdrawalcurrencyTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.withdrawalcurrencyTitle.setObjectName("withdrawalcurrencyTitle")
        self.withdrawalcurrencyText = QtWidgets.QLabel(self.withdrawalcurrencyPage)
        self.withdrawalcurrencyText.setGeometry(QtCore.QRect(-10, 260, 1111, 51))
        self.withdrawalcurrencyText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.withdrawalcurrencyText.setAlignment(QtCore.Qt.AlignCenter)
        self.withdrawalcurrencyText.setObjectName("withdrawalcurrencyText")
        self.cediBtn = QtWidgets.QPushButton(self.withdrawalcurrencyPage)
        self.cediBtn.setGeometry(QtCore.QRect(300, 390, 181, 71))
        self.cediBtn.setObjectName("cediBtn")
        self.dollarBtn = QtWidgets.QPushButton(self.withdrawalcurrencyPage)
        self.dollarBtn.setGeometry(QtCore.QRect(610, 390, 181, 71))
        self.dollarBtn.setObjectName("dollarBtn")
        self.main.addWidget(self.withdrawalcurrencyPage)


        ##########################################################################
        #### WITHDRAWAL AMOUNT PAGE
        ##########################################################################
        self.withdrawalamountPage = QtWidgets.QWidget()
        self.withdrawalamountPage.setStyleSheet("#withdrawalamountPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.withdrawalamountPage.setObjectName("withdrawalamountPage")
        self.frame_5 = QtWidgets.QFrame(self.withdrawalamountPage)
        self.frame_5.setGeometry(QtCore.QRect(290, 150, 571, 371))
        self.frame_5.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.currencyText = QtWidgets.QLabel(self.frame_5)
        self.currencyText.setGeometry(QtCore.QRect(10, 120, 551, 51))
        self.currencyText.setStyleSheet("background: none;\n""font-size: 30px;")

        self.currencyText.setAlignment(QtCore.Qt.AlignCenter)
        self.currencyText.setObjectName("currencyText")
        self.withdrawalamountInput = QtWidgets.QLineEdit(self.frame_5)
        self.withdrawalamountInput.setGeometry(QtCore.QRect(160, 180, 261, 81))
        self.withdrawalamountInput.setStyleSheet("font-weight: bold;\n""font-size: 30px;")

        self.withdrawalamountInput.setMaxLength(4)
        self.withdrawalamountInput.setAlignment(QtCore.Qt.AlignCenter)
        self.withdrawalamountInput.setPlaceholderText("")
        self.withdrawalamountInput.setObjectName("withdrawalamountInput")
        self.withdrawalSubmitBtn = QtWidgets.QPushButton(self.frame_5)
        self.withdrawalSubmitBtn.setGeometry(QtCore.QRect(210, 280, 161, 61))
        self.withdrawalSubmitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.withdrawalSubmitBtn.setStyleSheet("    background: rgba(0, 0, 0, 200);\n""    border-radius: 10px;\n""    font-size: 25px;\n""")

        self.withdrawalSubmitBtn.setObjectName("withdrawalSubmitBtn")
        self.withdrawalamountTitle = QtWidgets.QLabel(self.frame_5)
        self.withdrawalamountTitle.setGeometry(QtCore.QRect(4, 20, 561, 101))
        self.withdrawalamountTitle.setStyleSheet("background: none;\n""font-size: 40px;")

        self.withdrawalamountTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.withdrawalamountTitle.setObjectName("withdrawalamountTitle")
        self.main.addWidget(self.withdrawalamountPage)


        ##########################################################################
        #### CONFIRM WITHDRAWAL AMOUNT PAGE
        ##########################################################################
        self.confirmwithdrawalPage = QtWidgets.QWidget()
        self.confirmwithdrawalPage.setStyleSheet("#confirmwithdrawalPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.confirmwithdrawalPage.setObjectName("confirmwithdrawalPage")
        self.confirmwithdrawalText = QtWidgets.QLabel(self.confirmwithdrawalPage)
        self.confirmwithdrawalText.setGeometry(QtCore.QRect(0, 200, 1101, 121))
        self.confirmwithdrawalText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.confirmwithdrawalText.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmwithdrawalText.setObjectName("confirmwithdrawalText")
        self.confirmwithdrawYesBtn = QtWidgets.QPushButton(self.confirmwithdrawalPage)
        self.confirmwithdrawYesBtn.setGeometry(QtCore.QRect(350, 340, 141, 61))
        self.confirmwithdrawYesBtn.setStyleSheet("#confirmwithdrawYesBtn {\n""    background-color: #7ed957;\n""}\n""\n""#confirmwithdrawYesBtn:hover {\n""    background-color: #9df179;\n""}\n""\n""#confirmwithdrawYesBtn:pressed {\n""    background-color: #76c454;\n""}")

        self.confirmwithdrawYesBtn.setObjectName("confirmwithdrawYesBtn")
        self.confirmwithdrawNoBtn = QtWidgets.QPushButton(self.confirmwithdrawalPage)
        self.confirmwithdrawNoBtn.setGeometry(QtCore.QRect(600, 340, 141, 61))
        self.confirmwithdrawNoBtn.setStyleSheet("#confirmwithdrawNoBtn {\n""    background-color: #ff1616;\n""}\n""\n""#confirmwithdrawNoBtn:hover {\n""    background-color: #f13c3c;\n""}\n""\n""#confirmwithdrawNoBtn:pressed {\n""    background-color: #c20707;\n""}")

        self.confirmwithdrawNoBtn.setObjectName("confirmwithdrawNoBtn")
        self.main.addWidget(self.confirmwithdrawalPage)

        self.cashwaitPage = QtWidgets.QWidget()
        self.cashwaitPage.setStyleSheet("#cashwaitPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")
        
        ##########################################################################
        #### CASH WAIT AMOUNT PAGE
        ##########################################################################
        self.cashwaitPage.setObjectName("cashwaitPage")
        self.cashwaitText = QtWidgets.QLabel(self.cashwaitPage)
        self.cashwaitText.setGeometry(QtCore.QRect(0, 210, 1101, 261))
        self.cashwaitText.setStyleSheet("background: none;\n""font-size: 70px;")

        self.cashwaitText.setAlignment(QtCore.Qt.AlignCenter)
        self.cashwaitText.setObjectName("cashwaitText")
        self.main.addWidget(self.cashwaitPage)


        ##########################################################################
        #### SUCCESSFUL WITHDRAWAL PAGE
        ##########################################################################
        self.successfulwithdrawalPage = QtWidgets.QWidget()
        self.successfulwithdrawalPage.setStyleSheet("#successfulwithdrawalPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.successfulwithdrawalPage.setObjectName("successfulwithdrawalPage")
        self.frame_6 = QtWidgets.QFrame(self.successfulwithdrawalPage)
        self.frame_6.setGeometry(QtCore.QRect(180, 200, 761, 381))
        self.frame_6.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.withdrawnamountText = QtWidgets.QLabel(self.frame_6)
        self.withdrawnamountText.setGeometry(QtCore.QRect(14, 30, 731, 51))
        self.withdrawnamountText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.withdrawnamountText.setAlignment(QtCore.Qt.AlignCenter)
        self.withdrawnamountText.setObjectName("withdrawnamountText")
        self.previousbalanceText = QtWidgets.QLabel(self.frame_6)
        self.previousbalanceText.setGeometry(QtCore.QRect(10, 130, 741, 51))
        self.previousbalanceText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.previousbalanceText.setAlignment(QtCore.Qt.AlignCenter)
        self.previousbalanceText.setObjectName("previousbalanceText")
        self.newbalanceText = QtWidgets.QLabel(self.frame_6)
        self.newbalanceText.setGeometry(QtCore.QRect(10, 220, 741, 51))
        self.newbalanceText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.newbalanceText.setAlignment(QtCore.Qt.AlignCenter)
        self.newbalanceText.setObjectName("newbalanceText")
        self.receiptoptionBtn = QtWidgets.QPushButton(self.frame_6)
        self.receiptoptionBtn.setGeometry(QtCore.QRect(260, 300, 231, 61))
        self.receiptoptionBtn.setStyleSheet("    background: #7ed957;\n""    border-radius: 10px;\n""    font-size: 25px;\n""")

        self.receiptoptionBtn.setObjectName("receiptoptionBtn")
        self.successTitle = QtWidgets.QLabel(self.successfulwithdrawalPage)
        self.successTitle.setGeometry(QtCore.QRect(0, 100, 1101, 81))
        self.successTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.successTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.successTitle.setObjectName("successTitle")
        self.main.addWidget(self.successfulwithdrawalPage)


        ##########################################################################
        #### RECEIPT REQUEST PAGE
        ##########################################################################
        self.receiptrequestPage = QtWidgets.QWidget()
        self.receiptrequestPage.setStyleSheet("#receiptrequestPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.receiptrequestPage.setObjectName("receiptrequestPage")
        self.confirmreceiptNoBtn = QtWidgets.QPushButton(self.receiptrequestPage)
        self.confirmreceiptNoBtn.setGeometry(QtCore.QRect(600, 330, 141, 61))
        self.confirmreceiptNoBtn.setStyleSheet("#confirmreceiptNoBtn {\n""    background-color: #ff1616;\n""}\n""\n""#confirmreceiptNoBtn:hover {\n""    background-color: #f13c3c;\n""}\n""\n""#confirmreceiptNoBtn:pressed {\n""    background-color: #c20707;\n""}")

        self.confirmreceiptNoBtn.setObjectName("confirmreceiptNoBtn")
        self.receiptrequestText = QtWidgets.QLabel(self.receiptrequestPage)
        self.receiptrequestText.setGeometry(QtCore.QRect(0, 160, 1101, 121))
        self.receiptrequestText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.receiptrequestText.setAlignment(QtCore.Qt.AlignCenter)
        self.receiptrequestText.setObjectName("receiptrequestText")
        self.confirmreceiptYesBtn = QtWidgets.QPushButton(self.receiptrequestPage)
        self.confirmreceiptYesBtn.setGeometry(QtCore.QRect(350, 330, 141, 61))
        self.confirmreceiptYesBtn.setStyleSheet("#confirmreceiptYesBtn {\n""    background-color: #7ed957;\n""}\n""\n""#confirmreceiptYesBtn:hover {\n""    background-color: #9df179;\n""}\n""\n""#confirmreceiptYesBtn:pressed {\n""    background-color: #76c454;\n""}")

        self.confirmreceiptYesBtn.setObjectName("confirmreceiptYesBtn")
        self.main.addWidget(self.receiptrequestPage)



        ##########################################################################
        #### RECEIPT PAGE
        ##########################################################################
        self.receiptPage = QtWidgets.QWidget()
        self.receiptPage.setStyleSheet("#receiptPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.receiptPage.setObjectName("receiptPage")
        self.frame_7 = QtWidgets.QFrame(self.receiptPage)
        self.frame_7.setGeometry(QtCore.QRect(160, 190, 761, 411))
        self.frame_7.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.ReceipttransactionnumberText = QtWidgets.QLabel(self.frame_7)
        self.ReceipttransactionnumberText.setGeometry(QtCore.QRect(30, 20, 701, 51))
        self.ReceipttransactionnumberText.setStyleSheet("background: none;\n""font-size: 30px;")

        self.ReceipttransactionnumberText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ReceipttransactionnumberText.setObjectName("ReceipttransactionnumberText")
        self.ReceiptaccountnameText = QtWidgets.QLabel(self.frame_7)
        self.ReceiptaccountnameText.setGeometry(QtCore.QRect(30, 80, 701, 51))
        self.ReceiptaccountnameText.setStyleSheet("background: none;\n""font-size: 30px;")

        self.ReceiptaccountnameText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ReceiptaccountnameText.setObjectName("ReceiptaccountnameText")
        self.ReceiptamountwithdrawnText = QtWidgets.QLabel(self.frame_7)
        self.ReceiptamountwithdrawnText.setGeometry(QtCore.QRect(30, 140, 701, 51))
        self.ReceiptamountwithdrawnText.setStyleSheet("background: none;\n""font-size: 30px;")

        self.ReceiptamountwithdrawnText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ReceiptamountwithdrawnText.setObjectName("ReceiptamountwithdrawnText")
        self.ReceiptnewbalanceText2 = QtWidgets.QLabel(self.frame_7)
        self.ReceiptnewbalanceText2.setGeometry(QtCore.QRect(30, 200, 701, 51))
        self.ReceiptnewbalanceText2.setStyleSheet("background: none;\n""font-size: 30px;")

        self.ReceiptnewbalanceText2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ReceiptnewbalanceText2.setObjectName("ReceiptnewbalanceText2")
        self.thankyouText = QtWidgets.QLabel(self.frame_7)
        self.thankyouText.setGeometry(QtCore.QRect(10, 290, 741, 101))
        self.thankyouText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.thankyouText.setAlignment(QtCore.Qt.AlignCenter)
        self.thankyouText.setObjectName("thankyouText")
        self.receiptTitle = QtWidgets.QLabel(self.receiptPage)
        self.receiptTitle.setGeometry(QtCore.QRect(0, 100, 1101, 81))
        self.receiptTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.receiptTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.receiptTitle.setObjectName("receiptTitle")
        self.backtoMenuBtn2 = QtWidgets.QPushButton(self.receiptPage)
        self.backtoMenuBtn2.setGeometry(QtCore.QRect(820, 40, 231, 61))
        self.backtoMenuBtn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backtoMenuBtn2.setStyleSheet("    background: #7ed957;\n""    border-radius: 10px;\n""    font-size: 25px;\n""")

        self.backtoMenuBtn2.setObjectName("backtoMenuBtn2")
        self.main.addWidget(self.receiptPage)


        ##########################################################################
        #### PERFORM NEW TRANSACTION PAGE
        ##########################################################################
        self.newtransactionPage = QtWidgets.QWidget()
        self.newtransactionPage.setStyleSheet("#newtransactionPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.newtransactionPage.setObjectName("newtransactionPage")
        self.newtransactionNoBtn = QtWidgets.QPushButton(self.newtransactionPage)
        self.newtransactionNoBtn.setGeometry(QtCore.QRect(600, 340, 141, 61))
        self.newtransactionNoBtn.setStyleSheet("#newtransactionNoBtn {\n""    background-color: #ff1616;\n""}\n""\n""#newtransactionNoBtn:hover {\n""    background-color: #f13c3c;\n""}\n""\n""#newtransactionNoBtn:pressed {\n""    background-color: #c20707;\n""}")

        self.newtransactionNoBtn.setObjectName("newtransactionNoBtn")
        self.newtransactionText = QtWidgets.QLabel(self.newtransactionPage)
        self.newtransactionText.setGeometry(QtCore.QRect(0, 190, 1101, 121))
        self.newtransactionText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.newtransactionText.setAlignment(QtCore.Qt.AlignCenter)
        self.newtransactionText.setObjectName("newtransactionText")
        self.newtransactionYesBtn = QtWidgets.QPushButton(self.newtransactionPage)
        self.newtransactionYesBtn.setGeometry(QtCore.QRect(350, 340, 141, 61))
        self.newtransactionYesBtn.setStyleSheet("#newtransactionYesBtn {\n""    background-color: #7ed957;\n""}\n""\n""#newtransactionYesBtn:hover {\n""    background-color: #9df179;\n""}\n""\n""#newtransactionYesBtn:pressed {\n""    background-color: #76c454;\n""}")

        self.newtransactionYesBtn.setObjectName("newtransactionYesBtn")
        self.main.addWidget(self.newtransactionPage)


        ##########################################################################
        #### MOMO MENU PAGE
        ##########################################################################
        self.momomenuPage = QtWidgets.QWidget()
        self.momomenuPage.setStyleSheet("#momomenuPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")
                                        
        self.momomenuPage.setObjectName("momomenuPage")
        self.airtelBtn = QtWidgets.QPushButton(self.momomenuPage)
        self.airtelBtn.setGeometry(QtCore.QRect(40, 430, 291, 81))
        self.airtelBtn.setObjectName("airtelBtn")
        self.vodafoneBtn = QtWidgets.QPushButton(self.momomenuPage)
        self.vodafoneBtn.setGeometry(QtCore.QRect(770, 430, 291, 81))
        self.vodafoneBtn.setObjectName("vodafoneBtn")
        self.momoText = QtWidgets.QLabel(self.momomenuPage)
        self.momoText.setGeometry(QtCore.QRect(10, 290, 1071, 71))
        self.momoText.setStyleSheet("background: none;\n""font-size: 30px;")

        self.momoText.setAlignment(QtCore.Qt.AlignCenter)
        self.momoText.setObjectName("momoText")
        self.mtnBtn = QtWidgets.QPushButton(self.momomenuPage)
        self.mtnBtn.setGeometry(QtCore.QRect(400, 430, 291, 81))
        self.mtnBtn.setObjectName("mtnBtn")
        self.momoTitle = QtWidgets.QLabel(self.momomenuPage)
        self.momoTitle.setGeometry(QtCore.QRect(10, 150, 1071, 131))
        self.momoTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.momoTitle.setObjectName("momoTitle")
        self.mainmenuBtn2 = QtWidgets.QPushButton(self.momomenuPage)
        self.mainmenuBtn2.setGeometry(QtCore.QRect(840, 30, 231, 71))
        self.mainmenuBtn2.setStyleSheet("font-size: 25px;\n""font-weight: bold;")

        self.mainmenuBtn2.setObjectName("mainmenuBtn2")
        self.main.addWidget(self.momomenuPage)


        ##########################################################################
        #### MOMO TRANSACTION CODE PAGE
        ##########################################################################
        self.transactioncodePage = QtWidgets.QWidget()
        self.transactioncodePage.setStyleSheet("#transactioncodePage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.transactioncodePage.setObjectName("transactioncodePage")
        self.frame_8 = QtWidgets.QFrame(self.transactioncodePage)
        self.frame_8.setGeometry(QtCore.QRect(629, 259, 311, 301))
        self.frame_8.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;\n""\n""")

        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.transcodeInputTitle = QtWidgets.QLabel(self.frame_8)
        self.transcodeInputTitle.setGeometry(QtCore.QRect(10, 40, 291, 41))
        self.transcodeInputTitle.setStyleSheet("background: none;\n""font-size: 30px;")

        self.transcodeInputTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.transcodeInputTitle.setObjectName("transcodeInputTitle")
        self.transactioncodeInput = QtWidgets.QLineEdit(self.frame_8)
        self.transactioncodeInput.setGeometry(QtCore.QRect(20, 110, 261, 61))
        self.transactioncodeInput.setMaxLength(6)
        self.transactioncodeInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.transactioncodeInput.setAlignment(QtCore.Qt.AlignCenter)
        self.transactioncodeInput.setObjectName("transactioncodeInput")
        self.transcodeSubmitBtn = QtWidgets.QPushButton(self.frame_8)
        self.transcodeSubmitBtn.setGeometry(QtCore.QRect(90, 200, 131, 51))
        self.transcodeSubmitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.transcodeSubmitBtn.setStyleSheet("#transcodeSubmitBtn {\n""    background: rgba(0, 0, 0, 200);\n""    border-radius: 10px;\n""    font-size: 25px;\n""}\n""")

        self.transcodeSubmitBtn.setObjectName("transcodeSubmitBtn")
        self.transactioncodeTitle = QtWidgets.QLabel(self.transactioncodePage)
        self.transactioncodeTitle.setGeometry(QtCore.QRect(0, 120, 1101, 91))
        self.transactioncodeTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.transactioncodeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.transactioncodeTitle.setObjectName("transactioncodeTitle")
        self.frame_9 = QtWidgets.QFrame(self.transactioncodePage)
        self.frame_9.setGeometry(QtCore.QRect(120, 290, 411, 241))
        self.frame_9.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.transactioncodeText = QtWidgets.QLabel(self.frame_9)
        self.transactioncodeText.setGeometry(QtCore.QRect(10, 120, 391, 61))
        self.transactioncodeText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.transactioncodeText.setAlignment(QtCore.Qt.AlignCenter)
        self.transactioncodeText.setObjectName("transactioncodeText")
        self.transcodeParagraph = QtWidgets.QLabel(self.frame_9)
        self.transcodeParagraph.setGeometry(QtCore.QRect(10, 30, 391, 81))
        self.transcodeParagraph.setStyleSheet("background: none;\n""font-size: 25px;\n""font-weight: normal;")
        
        self.transcodeParagraph.setAlignment(QtCore.Qt.AlignCenter)
        self.transcodeParagraph.setObjectName("transcodeParagraph")
        self.line_3 = QtWidgets.QFrame(self.transactioncodePage)
        self.line_3.setGeometry(QtCore.QRect(550, 240, 20, 341))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.main.addWidget(self.transactioncodePage)


        ##########################################################################
        #### MOMO WITHDRAWAL PAGE
        ##########################################################################
        self.momowithdrawPage = QtWidgets.QWidget()
        self.momowithdrawPage.setStyleSheet("#momowithdrawPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.momowithdrawPage.setObjectName("momowithdrawPage")
        self.frame_10 = QtWidgets.QFrame(self.momowithdrawPage)
        self.frame_10.setGeometry(QtCore.QRect(310, 160, 571, 371))
        self.frame_10.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.momocurrencyText = QtWidgets.QLabel(self.frame_10)
        self.momocurrencyText.setGeometry(QtCore.QRect(10, 90, 551, 51))
        self.momocurrencyText.setStyleSheet("background: none;\n""font-size: 30px;")

        self.momocurrencyText.setAlignment(QtCore.Qt.AlignCenter)
        self.momocurrencyText.setObjectName("momocurrencyText")
        self.momowithdrawamountInput = QtWidgets.QLineEdit(self.frame_10)
        self.momowithdrawamountInput.setGeometry(QtCore.QRect(160, 170, 261, 81))
        self.momowithdrawamountInput.setStyleSheet("font-weight: bold;\n""font-size: 30px;")

        self.momowithdrawamountInput.setMaxLength(4)
        self.momowithdrawamountInput.setAlignment(QtCore.Qt.AlignCenter)
        self.momowithdrawamountInput.setPlaceholderText("")
        self.momowithdrawamountInput.setObjectName("momowithdrawamountInput")
        self.momowithdrawSubmitBtn = QtWidgets.QPushButton(self.frame_10)
        self.momowithdrawSubmitBtn.setGeometry(QtCore.QRect(210, 280, 161, 61))
        self.momowithdrawSubmitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.momowithdrawSubmitBtn.setStyleSheet("    background: rgba(0, 0, 0, 200);\n""    border-radius: 10px;\n""    font-size: 25px;\n" "")

        self.momowithdrawSubmitBtn.setObjectName("momowithdrawSubmitBtn")
        self.momowithdrawTitle = QtWidgets.QLabel(self.frame_10)
        self.momowithdrawTitle.setGeometry(QtCore.QRect(4, 20, 561, 51))
        self.momowithdrawTitle.setStyleSheet("background: none;\n""font-size: 40px;")

        self.momowithdrawTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.momowithdrawTitle.setObjectName("momowithdrawTitle")
        self.main.addWidget(self.momowithdrawPage)


        ##########################################################################
        #### MOMO CONFIRM WITHDRAWAL PAGE
        ##########################################################################
        self.momoconfirmPage = QtWidgets.QWidget()
        self.momoconfirmPage.setStyleSheet("#momoconfirmPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.momoconfirmPage.setObjectName("momoconfirmPage")
        self.momoconfirmwithdrawNoBtn = QtWidgets.QPushButton(self.momoconfirmPage)
        self.momoconfirmwithdrawNoBtn.setGeometry(QtCore.QRect(600, 330, 141, 61))
        self.momoconfirmwithdrawNoBtn.setStyleSheet("#momoconfirmwithdrawNoBtn {\n""    background-color: #ff1616;\n""}\n""\n""#momoconfirmwithdrawNoBtn:hover {\n""    background-color: #f13c3c;\n""}\n""\n""#momoconfirmwithdrawNoBtn:pressed {\n""    background-color: #c20707;\n""}")

        self.momoconfirmwithdrawNoBtn.setObjectName("momoconfirmwithdrawNoBtn")
        self.momoconfirmwithdrawalText = QtWidgets.QLabel(self.momoconfirmPage)
        self.momoconfirmwithdrawalText.setGeometry(QtCore.QRect(0, 190, 1101, 121))
        self.momoconfirmwithdrawalText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.momoconfirmwithdrawalText.setAlignment(QtCore.Qt.AlignCenter)
        self.momoconfirmwithdrawalText.setObjectName("momoconfirmwithdrawalText")
        self.momoconfirmwithdrawYesBtn = QtWidgets.QPushButton(self.momoconfirmPage)
        self.momoconfirmwithdrawYesBtn.setGeometry(QtCore.QRect(350, 330, 141, 61))
        self.momoconfirmwithdrawYesBtn.setStyleSheet("#momoconfirmwithdrawYesBtn {\n""    background-color: #7ed957;\n""}\n""\n""#momoconfirmwithdrawYesBtn:hover {\n""    background-color: #9df179;\n""}\n""\n""#momoconfirmwithdrawYesBtn:pressed {\n""    background-color: #76c454;\n""}")

        self.momoconfirmwithdrawYesBtn.setObjectName("momoconfirmwithdrawYesBtn")
        self.main.addWidget(self.momoconfirmPage)


        ##########################################################################
        #### ENTER MOMO PIN PAGE
        ##########################################################################
        self.momopinPage = QtWidgets.QWidget()
        self.momopinPage.setStyleSheet("#momopinPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.momopinPage.setObjectName("momopinPage")
        self.frame_11 = QtWidgets.QFrame(self.momopinPage)
        self.frame_11.setGeometry(QtCore.QRect(121, 291, 411, 241))
        self.frame_11.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.momopinText = QtWidgets.QLabel(self.frame_11)
        self.momopinText.setGeometry(QtCore.QRect(10, 120, 391, 61))
        self.momopinText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.momopinText.setAlignment(QtCore.Qt.AlignCenter)
        self.momopinText.setObjectName("momopinText")
        self.momopinParagraph = QtWidgets.QLabel(self.frame_11)
        self.momopinParagraph.setGeometry(QtCore.QRect(10, 20, 391, 81))
        self.momopinParagraph.setStyleSheet("background: none;\n""font-size: 25px;\n""font-weight: normal;")
        
        self.momopinParagraph.setAlignment(QtCore.Qt.AlignCenter)
        self.momopinParagraph.setObjectName("momopinParagraph")
        self.momopinTitle = QtWidgets.QLabel(self.momopinPage)
        self.momopinTitle.setGeometry(QtCore.QRect(1, 121, 1101, 91))
        self.momopinTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.momopinTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.momopinTitle.setObjectName("momopinTitle")
        self.line_4 = QtWidgets.QFrame(self.momopinPage)
        self.line_4.setGeometry(QtCore.QRect(551, 241, 20, 341))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.frame_12 = QtWidgets.QFrame(self.momopinPage)
        self.frame_12.setGeometry(QtCore.QRect(630, 300, 311, 221))
        self.frame_12.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;\n""\n""")

        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.momopinInput = QtWidgets.QLineEdit(self.frame_12)
        self.momopinInput.setGeometry(QtCore.QRect(20, 40, 261, 61))
        self.momopinInput.setMaxLength(4)
        self.momopinInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.momopinInput.setAlignment(QtCore.Qt.AlignCenter)
        self.momopinInput.setObjectName("momopinInput")
        self.momopinSubmitBtn = QtWidgets.QPushButton(self.frame_12)
        self.momopinSubmitBtn.setGeometry(QtCore.QRect(90, 130, 131, 51))
        self.momopinSubmitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.momopinSubmitBtn.setStyleSheet("#momopinSubmitBtn {\n""    background: rgba(0, 0, 0, 200);\n" "    border-radius: 10px;\n""    font-size: 25px;\n""}\n""")

        self.momopinSubmitBtn.setObjectName("momopinSubmitBtn")
        self.main.addWidget(self.momopinPage)


        ##########################################################################
        #### MOMO SUCCESS PAGE
        ##########################################################################
        self.momosuccessPage = QtWidgets.QWidget()
        self.momosuccessPage.setStyleSheet("#momosuccessPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.momosuccessPage.setObjectName("momosuccessPage")
        self.backtoMenuBtn3 = QtWidgets.QPushButton(self.momosuccessPage)
        self.backtoMenuBtn3.setGeometry(QtCore.QRect(820, 40, 231, 61))
        self.backtoMenuBtn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backtoMenuBtn3.setStyleSheet("    background: #7ed957;\n""    border-radius: 10px;\n""    font-size: 25px;\n""")

        self.backtoMenuBtn3.setObjectName("backtoMenuBtn3")
        self.momosuccessTitle = QtWidgets.QLabel(self.momosuccessPage)
        self.momosuccessTitle.setGeometry(QtCore.QRect(0, 140, 1101, 81))
        self.momosuccessTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.momosuccessTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.momosuccessTitle.setObjectName("momosuccessTitle")
        self.frame_13 = QtWidgets.QFrame(self.momosuccessPage)
        self.frame_13.setGeometry(QtCore.QRect(160, 290, 761, 231))
        self.frame_13.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.momosuccessText = QtWidgets.QLabel(self.frame_13)
        self.momosuccessText.setGeometry(QtCore.QRect(10, 60, 741, 101))
        self.momosuccessText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.momosuccessText.setAlignment(QtCore.Qt.AlignCenter)
        self.momosuccessText.setObjectName("momosuccessText")
        self.main.addWidget(self.momosuccessPage)


        ##########################################################################
        #### ACCOUNT BALANCE PAGE
        ##########################################################################
        self.balancePage = QtWidgets.QWidget()
        self.balancePage.setStyleSheet("#balancePage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n" "}")

        self.balancePage.setObjectName("balancePage")
        self.frame_14 = QtWidgets.QFrame(self.balancePage)
        self.frame_14.setGeometry(QtCore.QRect(160, 230, 761, 311))
        self.frame_14.setStyleSheet("background: rgba(0, 0, 0, 50);\n""border-radius: 20px;")

        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.balanceText = QtWidgets.QLabel(self.frame_14)
        self.balanceText.setGeometry(QtCore.QRect(10, 30, 741, 151))
        self.balanceText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.balanceText.setAlignment(QtCore.Qt.AlignCenter)
        self.balanceText.setObjectName("balanceText")
        self.backtoMenuBtn4 = QtWidgets.QPushButton(self.frame_14)
        self.backtoMenuBtn4.setGeometry(QtCore.QRect(260, 210, 231, 61))
        self.backtoMenuBtn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backtoMenuBtn4.setStyleSheet("    background: #7ed957;\n""    border-radius: 10px;\n""    font-size: 25px;\n""")

        self.backtoMenuBtn4.setObjectName("backtoMenuBtn4")
        self.balanceTitle = QtWidgets.QLabel(self.balancePage)
        self.balanceTitle.setGeometry(QtCore.QRect(0, 130, 1101, 81))
        self.balanceTitle.setStyleSheet("background: none;\n""font-size: 70px;")

        self.balanceTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.balanceTitle.setObjectName("balanceTitle")
        self.main.addWidget(self.balancePage)


        ##########################################################################
        #### LOGOUT CONFIRMATION PAGE
        ##########################################################################
        self.confirmquitPage = QtWidgets.QWidget()
        self.confirmquitPage.setStyleSheet("#confirmquitPage {\n""    background-image: url(:/assets/guiImages/languageBG.png);\n""}")

        self.confirmquitPage.setObjectName("confirmquitPage")
        self.confirmquitText = QtWidgets.QLabel(self.confirmquitPage)
        self.confirmquitText.setGeometry(QtCore.QRect(0, 180, 1101, 121))
        self.confirmquitText.setStyleSheet("background: none;\n""font-size: 40px;")

        self.confirmquitText.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmquitText.setObjectName("confirmquitText")
        self.confirmquitYesBtn = QtWidgets.QPushButton(self.confirmquitPage)
        self.confirmquitYesBtn.setGeometry(QtCore.QRect(350, 320, 141, 61))
        self.confirmquitYesBtn.setStyleSheet("#confirmquitYesBtn {\n""    background-color: #7ed957;\n""}\n""\n""#confirmquitYesBtn:hover {\n""    background-color: #9df179;\n""}\n""\n""#confirmquitYesBtn:pressed {\n""    background-color: #76c454;\n""}")

        self.confirmquitYesBtn.setObjectName("confirmquitYesBtn")
        self.confirmquitNoBtn = QtWidgets.QPushButton(self.confirmquitPage)
        self.confirmquitNoBtn.setGeometry(QtCore.QRect(600, 320, 141, 61))
        self.confirmquitNoBtn.setStyleSheet("#confirmquitNoBtn {\n""    background-color: #ff1616;\n""}\n""\n""#confirmquitNoBtn:hover {\n""    background-color: #f13c3c;\n""}\n""\n""#confirmquitNoBtn:pressed {\n""    background-color: #c20707;\n""}")

        self.confirmquitNoBtn.setObjectName("confirmquitNoBtn")
        self.main.addWidget(self.confirmquitPage)


        ##########################################################################
        #### EXIT PAGE
        ##########################################################################
        self.exitPage = QtWidgets.QWidget()
        self.exitPage.setStyleSheet("background-image: url(:/assets/guiImages/exitBG.png);")
        self.exitPage.setObjectName("exitPage")
        self.main.addWidget(self.exitPage)
        TechSealsATM.setCentralWidget(self.body)

        self.retranslateUi(TechSealsATM)
        self.main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TechSealsATM)




##########################################################################
#### PLACEHOLDER TEXTS
##########################################################################
    def retranslateUi(self, TechSealsATM):
        _translate = QtCore.QCoreApplication.translate
        TechSealsATM.setWindowTitle(_translate("TechSealsATM", "Tech Seals Bank"))

        ########################## WELCOME PAGE ##################################
        ####################### START BUTTON TEXT ################################
        ##########################################################################
        self.startBtn.setText(_translate("TechSealsATM", "START"))

        ####################### LANGUAGE SELECTOR PAGE ###########################
        #############################  TITLE TEXT ################################
        ##########################################################################
        self.pageHead.setText(_translate("TechSealsATM", "Please Select a Language"))

        ####################### LANGUAGE SELECTOR PAGE ###########################
        ######################### ENGLISH BUTTON TEXT ############################
        ##########################################################################
        self.englishBtn.setText(_translate("TechSealsATM", "English"))

        ####################### LANGUAGE SELECTOR PAGE ###########################
        ########################### TWI BUTTON TEXT ##############################
        ##########################################################################
        self.twiBtn.setText(_translate("TechSealsATM", "Asante Twi"))


        ################################ LOGIN PAGE ##############################
        ############################# LOGIN BUTTON TEXT ##########################
        ##########################################################################
        self.loginBtn.setText(_translate("TechSealsATM", "LOG IN"))

        ################################ LOGIN PAGE ##############################
        ########################### CARDLESS BUTTON TEXT #########################
        ##########################################################################
        self.cardlessBtn.setText(_translate("TechSealsATM", "Cardless Service"))

        ################################ LOGIN PAGE ##############################
        ################################ TITLE TEXT ##############################
        ##########################################################################
        self.loginTitle.setText(_translate("TechSealsATM", "LOG IN"))

        ################################ LOGIN PAGE ##############################
        #################### USERNAME INPUT PLACEHOLDER TEXT #####################
        ##########################################################################
        self.usernameInput.setPlaceholderText(_translate("TechSealsATM", "USERNAME"))

        ################################ LOGIN PAGE ##############################
        ######################## PIN INPUT PLACEHOLDER TEXT ######################
        ##########################################################################
        self.loginpinInput.setPlaceholderText(_translate("TechSealsATM", "PIN"))


        ############################ FORGOT PIN PAGE #############################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.forgotpinTitle.setText(_translate("TechSealsATM", "FORGOT PIN?"))

        ############################ FORGOT PIN PAGE #############################
        ############################ NO BUTTON TEXT ##############################
        ##########################################################################
        self.fpNoBtn.setText(_translate("TechSealsATM", "NO"))

        ############################ FORGOT PIN PAGE #############################
        ############################ YES BUTTON TEXT #############################
        ##########################################################################
        self.fpYesBtn.setText(_translate("TechSealsATM", "YES"))

        ############################ FORGOT PIN PAGE #############################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.forgotpinText.setText(_translate("TechSealsATM", "Would you like to change your pin?"))


        ######################## VERIFICATION CODE PAGE ##########################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.verificationcodeTitle.setText(_translate("TechSealsATM", "VERIFICATION CODE"))

        ######################## VERIFICATION CODE PAGE ##########################
        ################################ CODE TEXT ###############################
        ##########################################################################
        self.verificationcodeText.setText(_translate("TechSealsATM", "682386"))

        ######################## VERIFICATION CODE PAGE ##########################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.vericodeParagraph.setText(_translate("TechSealsATM", "A Verification Code has been sent\n""to your Mobile number"))
        
        ######################## VERIFICATION CODE PAGE ##########################
        ########################### INSTRUCTION TEXT #############################
        ##########################################################################
        self.vericodeInputTitle.setText(_translate("TechSealsATM", "Enter code here"))

        ######################## VERIFICATION CODE PAGE ##########################
        ##################### CODE INPUT PLACEHOLDER TEXT ########################
        ##########################################################################
        self.verificationcodeInput.setPlaceholderText(_translate("TechSealsATM", "VERIFICATION CODE"))

        ######################## VERIFICATION CODE PAGE ##########################
        ########################## SUBMIT BUTTON TEXT ############################
        ##########################################################################
        self.vericodeSubmitBtn.setText(_translate("TechSealsATM", "SUBMIT"))


        ############################## PIN CHANGE PAGE ###########################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.pinchangeTitle.setText(_translate("TechSealsATM", "PIN CHANGE"))

        ############################## PIN CHANGE PAGE ###########################
        ############################ CONFIRM BUTTON TEXT #########################
        ##########################################################################
        self.pinchangeConfirmBtn.setText(_translate("TechSealsATM", "CONFIRM"))

        ############################## PIN CHANGE PAGE ###########################
        ########################## NEW PIN PLACEHOLDER TEXT ######################
        ##########################################################################
        self.newpinInput.setPlaceholderText(_translate("TechSealsATM", "ENTER NEW PIN"))

        ############################## PIN CHANGE PAGE ###########################
        ##################### RE-ENTER NEW PIN PLACEHOLDER TEXT ##################
        ##########################################################################
        self.newpinconfirmInput.setPlaceholderText(_translate("TechSealsATM", "RE-ENTER PIN"))


        ############################## ATM MENU PAGE #############################
        ################################ TITLE TEXT ##############################
        ##########################################################################
        self.welcomeTitle.setText(_translate("TechSealsATM", "Welcome USERNAME"))

        ############################## ATM MENU PAGE #############################
        ################################# BODY TEXT ##############################
        ##########################################################################
        self.welcomeText.setText(_translate("TechSealsATM", "What would you like to do today?"))

        ############################## ATM MENU PAGE #############################
        ########################### BALANCE BUTTON TEXT ##########################
        ##########################################################################
        self.balanceBtn.setText(_translate("TechSealsATM", "Check Balance"))

        ############################## ATM MENU PAGE #############################
        ######################### WITHDRAWAL BUTTON TEXT #########################
        ##########################################################################
        self.withdrawalBtn.setText(_translate("TechSealsATM", "Withdrawal"))

        ############################## ATM MENU PAGE #############################
        ############################ MOMO BUTTON TEXT ############################
        ##########################################################################
        self.momoBtn.setText(_translate("TechSealsATM", "Mobile Money"))

        ############################## ATM MENU PAGE #############################
        ############################ LOGOUT BUTTON TEXT ##########################
        ##########################################################################
        self.logoutBtn.setText(_translate("TechSealsATM", "LOG OUT"))


        ######################## WITHDRAWAL CURENCY PAGE #########################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.withdrawalcurrencyTitle.setText(_translate("TechSealsATM", "WITHDRAWAL"))

        ######################## WITHDRAWAL CURENCY PAGE #########################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.withdrawalcurrencyText.setText(_translate("TechSealsATM", "Withdraw from Ghana Cedi or US Dollar account"))
        
        ######################## WITHDRAWAL CURENCY PAGE #########################
        ########################### CEDI BUTTON TEXT #############################
        ##########################################################################
        self.cediBtn.setText(_translate("TechSealsATM", "GHS"))

        ######################## WITHDRAWAL CURENCY PAGE #########################
        ########################## DOLLAR BUTTON TEXT ############################
        ##########################################################################
        self.dollarBtn.setText(_translate("TechSealsATM", "USD"))


        ######################### WITHDRAWAL AMOUNT PAGE #########################
        ############################# CURRENCY TEXT ##############################
        ##########################################################################
        self.currencyText.setText(_translate("TechSealsATM", "GHS"))

        ######################### WITHDRAWAL AMOUNT PAGE #########################
        ########################### SUBMIT BUTTON TEXT ###########################
        ##########################################################################
        self.withdrawalSubmitBtn.setText(_translate("TechSealsATM", "SUBMIT"))

        ######################### WITHDRAWAL AMOUNT PAGE #########################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.withdrawalamountTitle.setText(_translate("TechSealsATM", "Enter Withdrawal Amount"))


        ######################## CONFIRM WITHDRAWAL PAGE #########################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.confirmwithdrawalText.setText(_translate("TechSealsATM", "Confirm Withdrawal of GHS 1000"))

        ######################## CONFIRM WITHDRAWAL PAGE #########################
        ############################ YES BUTTON TEXT #############################
        ##########################################################################
        self.confirmwithdrawYesBtn.setText(_translate("TechSealsATM", "YES"))

        ######################## CONFIRM WITHDRAWAL PAGE #########################
        ############################# NO BUTTON TEXT #############################
        ##########################################################################
        self.confirmwithdrawNoBtn.setText(_translate("TechSealsATM", "NO"))


        ######################## CASH WAIT PAGE #########################
        ############################# BODY TEXT #############################
        ##########################################################################
        self.cashwaitText.setText(_translate("TechSealsATM", "DISPENSING CASH \n""PLEASE WAIT"))


        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ######################### WITHDRAWAL AMOUNT TEXT #########################
        ##########################################################################
        self.withdrawnamountText.setText(_translate("TechSealsATM", "Successful Withdrawal of GHS 1000"))

        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ########################## PREVIOUS BALANCE TEXT #########################
        ##########################################################################
        self.previousbalanceText.setText(_translate("TechSealsATM", "Previous Balance was GHS 5000"))

        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ############################ NEW BALANCE TEXT ############################
        ##########################################################################
        self.newbalanceText.setText(_translate("TechSealsATM", "New Balance is GHS 4000"))

        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ######################### BACK TO MAIN MENU TEXT #########################
        ##########################################################################
        self.receiptoptionBtn.setText(_translate("TechSealsATM", "DONE"))

        ####################### SUCCESSFUL WITHDRAWAL PAGE #######################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.successTitle.setText(_translate("TechSealsATM", "SUCCESS"))


        ########################## RECEIPT REQUEST PAGE ##########################
        ############################# NO BUTTON TEXT #############################
        ##########################################################################
        self.confirmreceiptNoBtn.setText(_translate("TechSealsATM", "NO"))

        ########################## RECEIPT REQUEST PAGE ##########################
        ############################### TITLE TEXT ###############################
        ##########################################################################
        self.receiptrequestText.setText(_translate("TechSealsATM", "Would you like a receipt for this \n""transaction?"))
        
        ########################## RECEIPT REQUEST PAGE ##########################
        ############################ YES BUTTON TEXT #############################
        ##########################################################################
        self.confirmreceiptYesBtn.setText(_translate("TechSealsATM", "YES"))


        ############################# RECEIPT PAGE ###############################
        ####################### TRANSACTION NUMBER TEXT ##########################
        ##########################################################################
        self.ReceipttransactionnumberText.setText(_translate("TechSealsATM", "Transaction Number: 21324568624"))

        ############################# RECEIPT PAGE ###############################
        ########################## ACCOUNT NAME TEXT #############################
        ##########################################################################
        self.ReceiptaccountnameText.setText(_translate("TechSealsATM", "Account Name: ABA"))

        ############################# RECEIPT PAGE ###############################
        ######################## WITHDRAWN AMOUNT TEXT ###########################
        ##########################################################################
        self.ReceiptamountwithdrawnText.setText(_translate("TechSealsATM", "Amount Withdrawn: GHS 1000"))

        ############################# RECEIPT PAGE ###############################
        ########################## NEW BALANCE TEXT ##############################
        ##########################################################################
        self.ReceiptnewbalanceText2.setText(_translate("TechSealsATM", "New Available Balance: GHS 4000"))

        ############################# RECEIPT PAGE ###############################
        ############################ THANK YOU TEXT ##############################
        ##########################################################################
        self.thankyouText.setText(_translate("TechSealsATM", "Thank you for choosing \nTech Seals Bank"))

        ############################# RECEIPT PAGE ###############################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.receiptTitle.setText(_translate("TechSealsATM", "RECEIPT"))

        ############################# RECEIPT PAGE ###############################
        #################### BACK TO MAIN MENU BUTTON TEXT #######################
        ##########################################################################
        self.backtoMenuBtn2.setText(_translate("TechSealsATM", "DONE"))


        ##################### PERFORM NEW TRANSACTION PAGE #######################
        ############################# NO BUTTON TEXT #############################
        ##########################################################################
        self.newtransactionNoBtn.setText(_translate("TechSealsATM", "NO"))

        ##################### PERFORM NEW TRANSACTION PAGE #######################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.newtransactionText.setText(_translate("TechSealsATM", "Would you want to perform another \ntransaction?"))
        
        ##################### PERFORM NEW TRANSACTION PAGE #######################
        ############################ YES BUTTON TEXT #############################
        ##########################################################################
        self.newtransactionYesBtn.setText(_translate("TechSealsATM", "YES"))


        ############################ MOMO MENU PAGE ##############################
        ######################## AIRTELTIGO BUTTON TEXT ##########################
        ##########################################################################
        self.airtelBtn.setText(_translate("TechSealsATM", "AIRTELTIGO"))

        ############################ MOMO MENU PAGE ##############################
        ########################## VODAFONE BUTTON TEXT ##########################
        ##########################################################################
        self.vodafoneBtn.setText(_translate("TechSealsATM", "VODAFONE"))

        ############################ MOMO MENU PAGE ##############################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.momoText.setText(_translate("TechSealsATM", "Select Your Network Provider"))

        ############################ MOMO MENU PAGE ##############################
        ############################ MTN BUTTON TEXT #############################
        ##########################################################################
        self.mtnBtn.setText(_translate("TechSealsATM", "MTN"))

        ############################ MOMO MENU PAGE ##############################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.momoTitle.setText(_translate("TechSealsATM", "MOBILE MONEY"))

        ############################ MOMO MENU PAGE ##############################
        ####################### BACK TO MAIN BUTTON TEXT #########################
        ##########################################################################
        self.mainmenuBtn2.setText(_translate("TechSealsATM", "BACK TO MAIN"))

        ######################## TRANSACTION CODE PAGE ###########################
        ##################### CODE INPUT INSTRUCTION TEXT ########################
        ##########################################################################
        self.transcodeInputTitle.setText(_translate("TechSealsATM", "Enter code here"))

        ######################## TRANSACTION CODE PAGE ###########################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.transactioncodeInput.setPlaceholderText(_translate("TechSealsATM", "TRANSACTION CODE"))

        ######################## TRANSACTION CODE PAGE ###########################
        ######################### SUBMIT BUTTON TEXT #############################
        ##########################################################################
        self.transcodeSubmitBtn.setText(_translate("TechSealsATM", "SUBMIT"))

        ######################## TRANSACTION CODE PAGE ###########################
        ############################# TITLE TEXT #################################
        ##########################################################################
        self.transactioncodeTitle.setText(_translate("TechSealsATM", "TRANSACTION CODE"))

        ######################## TRANSACTION CODE PAGE ###########################
        ############################## CODE TEXT #################################
        ##########################################################################
        self.transactioncodeText.setText(_translate("TechSealsATM", "682386"))

        ######################## TRANSACTION CODE PAGE ###########################
        ############################# BODY TEXT ##################################
        ##########################################################################
        self.transcodeParagraph.setText(_translate("TechSealsATM", "A Transaction Code has been sent\n""to your Mobile number"))
        
        
        ######################### MOMO WITHDRAWAL PAGE ###########################
        ############################# CURRENCY TEXT ##############################
        ##########################################################################
        self.momocurrencyText.setText(_translate("TechSealsATM", "GHS"))

        ######################### MOMO WITHDRAWAL PAGE ###########################
        ########################## SUBMIT BUTTON TEXT ############################
        ##########################################################################
        self.momowithdrawSubmitBtn.setText(_translate("TechSealsATM", "SUBMIT"))

        ######################### MOMO WITHDRAWAL PAGE ###########################
        ############################### BODY TEXT ################################
        ##########################################################################
        self.momowithdrawTitle.setText(_translate("TechSealsATM", "Enter Amount"))


        ##################### CONFIRM MOMO WITHDRAWAL PAGE #######################
        ########################### NO BUTTON TEXT ###############################
        ##########################################################################
        self.momoconfirmwithdrawNoBtn.setText(_translate("TechSealsATM", "NO"))

        ##################### CONFIRM MOMO WITHDRAWAL PAGE #######################
        ############################## TITLE TEXT ################################
        ##########################################################################
        self.momoconfirmwithdrawalText.setText(_translate("TechSealsATM", "Confirm Withdrawal of GHS "))

        ##################### CONFIRM MOMO WITHDRAWAL PAGE #######################
        ########################### YES BUTTON TEXT ##############################
        ##########################################################################
        self.momoconfirmwithdrawYesBtn.setText(_translate("TechSealsATM", "YES"))


        ####################### MOMO PIN CONFIRM PAGE ############################
        ############################# PIN TEXT ###################################
        ##########################################################################
        self.momopinText.setText(_translate("TechSealsATM", "9562"))

        ####################### MOMO PIN CONFIRM PAGE ############################
        ############################## BODY TEXT #################################
        ##########################################################################
        self.momopinParagraph.setText(_translate("TechSealsATM", "GENERIC MOBILE MONEY PIN"))

        ####################### MOMO PIN CONFIRM PAGE ############################
        ############################# TITLE TEXT #################################
        ##########################################################################
        self.momopinTitle.setText(_translate("TechSealsATM", "MOBILE MONEY PIN"))

        ####################### MOMO PIN CONFIRM PAGE ############################
        #################### PIN INPUT PLACEHOLDER TEXT ##########################
        ##########################################################################
        self.momopinInput.setPlaceholderText(_translate("TechSealsATM", "ENTER MOMO PIN"))

        ####################### MOMO PIN CONFIRM PAGE ############################
        #################### PIN INPUT PLACEHOLDER TEXT ##########################
        ##########################################################################
        self.momopinSubmitBtn.setText(_translate("TechSealsATM", "SUBMIT"))

        #################### MOMO WITHDRAW SUCCESS PAGE ##########################
        ################## BACK TO MAIN MENU BUTTON TEXT #########################
        ##########################################################################
        self.backtoMenuBtn3.setText(_translate("TechSealsATM", "DONE"))

        #################### MOMO WITHDRAW SUCCESS PAGE ##########################
        ############################ TITLE TEXT ##################################
        ##########################################################################
        self.momosuccessTitle.setText(_translate("TechSealsATM", "MOBILE MONEY"))

        #################### MOMO WITHDRAW SUCCESS PAGE ##########################
        ############################ BODY TEXT ###################################
        ##########################################################################
        self.momosuccessText.setText(_translate("TechSealsATM", "Successful Withdrawal!"))


        ####################### ACCOUNT BALANCE PAGE #############################
        ############################ BODY TEXT ###################################
        ##########################################################################
        self.balanceText.setText(_translate("TechSealsATM", "Your current GHS balance is\n""GHS 3000.00"))

        ####################### ACCOUNT BALANCE PAGE #############################
        ############################ BODY TEXT ###################################
        ##########################################################################
        self.backtoMenuBtn4.setText(_translate("TechSealsATM", "DONE"))

        ####################### ACCOUNT BALANCE PAGE #############################
        ############################ TITLE TEXT ##################################
        ##########################################################################
        self.balanceTitle.setText(_translate("TechSealsATM", "ACCOUNT BALANCE"))


        ######################## CONFIRM LOGOUT PAGE #############################
        ############################ TITLE TEXT ##################################
        ##########################################################################
        self.confirmquitText.setText(_translate("TechSealsATM", "Are you sure you want to Quit?"))

        ######################## CONFIRM LOGOUT PAGE #############################
        ########################## YES BUTTON TEXT ###############################
        ##########################################################################
        self.confirmquitYesBtn.setText(_translate("TechSealsATM", "YES"))

        ######################## CONFIRM LOGOUT PAGE #############################
        ########################### NO BUTTON TEXT ###############################
        ##########################################################################
        self.confirmquitNoBtn.setText(_translate("TechSealsATM", "NO"))




#################### IMPORT PROGRAM IMAGES ##########################
import images_rc
