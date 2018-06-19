'''
Created on Sep 24, 2015

@author: Riddhita.Sarcar
'''

'''
This class contains all the possible exceptions associated with DTH account recharge.
'''

class InvalidDTHOperatorException(Exception):
    def __init__(self):
        super().__init__("DTH Operator is invalid")
    

class InvalidCustomerIDException(Exception):
    def __init__(self):
        super().__init__("** INVALID CUSTOMER ID")
        

class InvalidPhoneNumberException(Exception):
    def __init__(self):
        super().__init__("** NOT A REGISTERED PHONE NUMBER")


class InvalidAmountException(Exception):
    def __init__(self):
        super().__init__("Minimum recharge amount is Rs. 200")
        
class InvalidDTHBalanceException(Exception):
    def __init__(self):
        super().__init__("Recharge unsuccessful. Not enough balance in account")
        
        