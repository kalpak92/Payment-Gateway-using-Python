'''
Created on Sep 26, 2015

@author: Riddhita.Sarcar
'''

from validations import Payment_Validations
from exceptions.Payment_Exceptions import *
from exceptions.Input_Exceptions import *
from database import Payment_DB


'''
This function is called when the customer enters the payment gateway
'''
def payment(amount):
    try:
        print("+~~~~~~~~~~~~~~~~~~~~~~~~~~+")
        print("$ SUPER PAYMENT GATEWAY $")
        print("+~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    
        card_number=input("Enter Card Number: ")
        customer_name=input("Enter Name: ")
        expiry_date=input("Enter Expiry Date (MM/YY):" )
        cvv=input("Enter CVV: ")
          
    
        list_of_details=Payment_Validations.validate_payment(card_number, customer_name, expiry_date, cvv)
        
        print("Card is valid. Type is "+list_of_details[0].get_card_type())
        
        result=Payment_DB.generate_grid_question(list_of_details)
        
        user_answer=input("Enter Grid Values ("+result[0]+"): ")
        
        if user_answer==result[1]:
            status=Payment_DB.transaction(list_of_details, amount)
            
            if not(status):
                raise InsufficientBalanceException
        return True
    
    
        
    except InvalidCardException as e:
        print(e)
        
    except InvalidNameException as e:
        print(e)
        
    except InvalidExpiryDateException as e:
        print(e)
        
    except ExpiredCardException as e:
        print(e)
        
    except InvalidCvvException as e:
        print(e)
        
    except InactiveCardException as e:
        print(e)
        
    except IncorrectGridValueException as e:
        print(e)
        
    except InsufficientBalanceException as e:
        print(e)


        
        
        