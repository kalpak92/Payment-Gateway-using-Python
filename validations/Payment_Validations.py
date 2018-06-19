'''
Created on Sep 26, 2015

@author: Riddhita.Sarcar
'''

from database import Payment_DB
from exceptions.Payment_Exceptions import InvalidCardException, InvalidNameException, InvalidExpiryDateException, ExpiredCardException, InvalidCvvException, InactiveCardException


'''
This function is used to validate the credentials of the Card Holder
'''
def validate_payment(card_number, customer_name, expiry_date, cvv):
    
    list_of_card_numbers=Payment_DB.get_card_number(card_number)
    if len(list_of_card_numbers)==0:
        raise InvalidCardException
    
    
    list_of_customer_names=Payment_DB.get_customer_name(customer_name, card_number)
    if len(list_of_customer_names)==0:
        raise InvalidNameException
    
    
    list_of_expiry_dates=Payment_DB.get_expiry_dates(expiry_date, card_number)
    if len(list_of_expiry_dates)==0:
        raise InvalidExpiryDateException
    
    
    status=Payment_DB.check_expiry_date(list_of_expiry_dates)
    if not(status):
        raise ExpiredCardException
    
    
    list_of_cvv=Payment_DB.get_cvv(cvv, card_number)
    if len(list_of_cvv)==0:
        raise InvalidCvvException
    
    
    list_of_status=Payment_DB.check_status(card_number)
    if len(list_of_status)==0:
        raise InactiveCardException
    
    
    list_of_details=Payment_DB.get_details(card_number)
    
    return list_of_details

