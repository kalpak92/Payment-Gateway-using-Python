'''
Created on Sep 24, 2015

@author: Riddhita.Sarcar
'''

'''
This function is used for validating the DTH operator name, Registered Phone Number, Customer ID
'''

from database import DTH_DB
from exceptions.DTH_Exceptions import InvalidDTHOperatorException, InvalidPhoneNumberException, InvalidCustomerIDException


def validate_recharge(operator_name, phone_no, acct_id):
    
    list_of_operators=DTH_DB.get_DTH_Operator(operator_name)
    if len(list_of_operators)==0:
        raise InvalidDTHOperatorException
    
    
    if phone_no!="":
        list_of_phone_numbers=DTH_DB.get_RMN(phone_no, list_of_operators[0].get_op_id())
        if len(list_of_phone_numbers)==0:
            raise InvalidPhoneNumberException
    
    
    if acct_id!="":
        list_of_account_ids=DTH_DB.get_Account_ID(acct_id, list_of_operators[0].get_op_id())
        if len(list_of_account_ids)==0:
            raise InvalidCustomerIDException
    
    
    
    list_of_details=DTH_DB.get_details(phone_no, acct_id)
    return list_of_details 