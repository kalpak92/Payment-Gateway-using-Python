'''
Created on Sep 26, 2015

@author: Riddhita.Sarcar
'''

class InvalidCardException(Exception):
    def __init__(self):
        super().__init__("Card not present in database")
    

class InvalidNameException(Exception):
    def __init__(self):
        super().__init__("Card Name does not match the data provided")
          

class InvalidExpiryDateException(Exception):
    def __init__(self):
        super().__init__("Expiry Date does not match the data provided")
        
        
class ExpiredCardException(Exception):
    def __init__(self):
        super().__init__("Card has expired")
        
    
class InvalidCvvException(Exception):
    def __init__(self):
        super().__init__("CVV does not match the data provided")
    
    
class InactiveCardException(Exception):
    def __init__(self):
        super().__init__("Card is inactive")
        
        
class IncorrectGridValueException(Exception):
    def __init__(self):
        super().__init__("Grid values do not match")
    

class  InsufficientBalanceException(Exception):
    def __init__(self):
        super().__init__("Account Balance Insufficient. Transaction cancelled.")
    
    