'''
Created on Sep 24, 2015

@author: Kalpak.Seal
'''

from database import Postpaid_DB
from exceptions.Postpaid_Exceptions import MobileDoesNotBelongToOperatorException, InvalidMobileNumberException, InvalidOperatorException, InvalidMobileTypeException 
from exceptions.Postpaid_Exceptions import InvalidAmountException



'''
This function is used to validate the details supplied by the user
'''
def validate_mobile_number(mobile_no, operator, amount):
    list_of_details = Postpaid_DB.get_mobile_in_operator(mobile_no, operator)
    
    list_of_mobileno = Postpaid_DB.get_mobile_no(mobile_no)
    
    list_of_operator = Postpaid_DB.get_operator(operator)
    
    list_of_type = Postpaid_DB.get_conn_type(mobile_no)
    
    balance = Postpaid_DB.get_balance(mobile_no)
    
    amt=float(amount)
    
    
    if(len(list_of_mobileno)==0):
        raise InvalidMobileNumberException
    
    
    elif(len(list_of_operator)==0):
        raise InvalidOperatorException
    
    
    elif (list_of_type.upper() == "PREPAID"):
        raise InvalidMobileTypeException
    
    
    elif (len(list_of_details)==0):
        raise MobileDoesNotBelongToOperatorException
    
    
    elif (amt < float(balance*0.8)) or (amt > float(balance*1.1)): 
        raise InvalidAmountException 
        
        
    return list_of_details




        