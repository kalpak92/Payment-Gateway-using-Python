'''
Created on Sep 24, 2015

@author: swayam.sarkar
'''
from database import Prepaid_DB
from exceptions.Prepaid_Exceptions import InvalidMobileNumberException, InvalidOperatorException, InvalidMobileOperatorException, InvalidTypeException    

'''
This function is used to validate the details supplied by the user
'''
def validate_mobile_number(phone_no, operator, amount):

    list_of_details = Prepaid_DB.get_phonenoinoperator(phone_no, operator)
    list_of_operator = Prepaid_DB.get_operator(operator)
    list_of_type = Prepaid_DB.get_conn_type(phone_no)
   
   
    if len(phone_no)!=10:   # is used to validate mobile number
        raise InvalidMobileNumberException()  
    
    
    elif(len(list_of_operator)==0):     # is used to validate the operator
        raise InvalidOperatorException       

    if list_of_type==False:
        raise InvalidMobileNumberException() 
    
    elif (list_of_type.upper() == "POSTPAID"):      # is used to validate if mobile number is prepaid
        raise InvalidTypeException

    
    elif (list_of_details==False):
        raise InvalidMobileOperatorException    # is used to validate the mobile number under an operator

    
    return True



