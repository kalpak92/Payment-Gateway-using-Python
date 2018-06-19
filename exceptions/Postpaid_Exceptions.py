'''
Created on Sep 24, 2015

@author: Kalpak.Seal
'''
'''
This file has all the custom exceptions needed for the project
'''


class InvalidMobileNumberException(Exception):
    def __init__(self):
        super().__init__("** INVALID MOBILE NUMBER")
        
        
        
class InvalidOperatorException(Exception):
    def __init__(self):
        super().__init__("** INVALID OPERATOR")
        


class MobileDoesNotBelongToOperatorException(Exception):
    def __init__(self):
        super().__init__("The mobile no. does not belong the given operator")
           
        
        
class InvalidMobileTypeException(Exception):
    def __init__(self):
        super().__init__("** CANNOT PAY BILL FOR PREPAID MOBILE")


        
class InvalidAmountException(Exception):
    def __init__(self):
        super().__init__("Invalid Amount")
        
