from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ATMapp import * 
from ATMgui import Ui_TechSealsATM
from functions import *

userArray=[{'username':'aba', 'pin':2121, 'balance':{'GHS':100000, 'USD':80000} },
{'username':'akosua', 'pin':4000, 'balance':{'GHS':280, 'USD':450} },
{'username':'eben', 'pin':5461, 'balance':{'GHS':800, 'USD':300} },
{'username':'bet', 'pin':3197, 'balance':{'GHS':995000, 'USD':980000} },
{'username':'david', 'pin':3216, 'balance':{'GHS':789, 'USD':250} },
{'username':'dna', 'pin':1234, 'balance':{'GHS':25000, 'USD':15000} },
{'username':'dave', 'pin':1034, 'balance':{'GHS':250, 'USD':8000} },
{'username':'esinam', 'pin':1110, 'balance':{'GHS':5000, 'USD':20000} },
{'username':'emmanuel', 'pin':2145, 'balance':{'GHS':8943, 'USD':2153} },
{'username':'van', 'pin':2111, 'balance':{'GHS':15000, 'USD':80000} },
{'username':'bagna', 'pin':7438, 'balance':{'GHS':555000, 'USD':300000} } ]

def userLogin(userName):


        for userdata in userArray:

            sessiondata = {'username':'unknown', 'pin':0000, 'balance':{'GHS':0, 'USD':0} } 

            # Checks for user existence and says a welcome message

            if userName == userdata['username']:
                found = True
                sessiondata = userdata #Transfers the found users bank info in to sessiondata variable
                break  
                
            else:
                found = False
                pass          

        
        return sessiondata # Returns the value of sessiondata after userLogin() is run,  so we can use in the continuing code 


    

def pinVerify(userPin, pin):
        
        valid = False
        
        for attempt in range(4):
            
            if userPin == pin :
                valid = True
                break

            else:
                valid = False
                continue
        
        
        
        
                
        return  valid




    


