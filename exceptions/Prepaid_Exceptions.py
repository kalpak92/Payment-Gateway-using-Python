'''
Created on Sep 24, 2015

@author: swayam.sarkar
'''


class InvalidMobileNumberException(Exception):
    def __init__(self):
        super().__init__("** INVALID MOBILE NUMBER")



class InvalidOperatorException(Exception):
    def __init__(self):
        super().__init__("** INVALID OPERATOR")
        
        
        
class InvalidMobileOperatorException(Exception):
    def __init__(self):
        super().__init__("** MOBILE NUMBER IS NOT PRESENT IN OPERATOR LIST")
        
        
        
class InvalidTypeException(Exception):
    def __init__(self):
        super().__init__("** CANNOT RECHARGE POSTPAID MOBILE")     
      
        
        
        