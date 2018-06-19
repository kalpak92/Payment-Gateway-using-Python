'''
Created on Sep 25, 2015

@author: athira.soman
'''

class InvalidOperatorException(Exception):
    def __init__(self):
        super().__init__("** INVALID OPERATOR")
        
        
        
class InvalidRechargeTypeException(Exception):
    def __init__(self):
        super().__init__("** INVALID RECHARGE TYPE")
        
        
        
class NoRechargeOptionException(Exception):
    def __init__(self):
        super().__init__("** NO RECHARGE OPTION")
        
        
        
class InvalidRangeException(Exception):
    def __init__(self):
        super().__init__("** INVALID RANGE")