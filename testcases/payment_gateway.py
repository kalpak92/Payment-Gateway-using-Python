'''
Created on Sep 28, 2015

@author: Riddhita.Sarcar
'''

from exceptions.Payment_Exceptions import InvalidCardException, InvalidNameException, InvalidExpiryDateException, InvalidCvvException, ExpiredCardException, InactiveCardException
from validations.Payment_Validations import validate_payment


print("Common Module : PAYMENT GATEWAY")




''' Positive test cases '''

print("Details provided for positive test case 1:-\n")
card_number="7437-8982-1769-4881"
cust_name="Debayan Sen"
exp_date="08/25"
cvv=274
print("Card Number: ", card_number)
print("Customer Name: ", cust_name)
print("Expiry Date: ", exp_date)
print("CVV: ", cvv)
print("Expected result : TRUE")
list_of_card_details=validate_payment(card_number, cust_name, exp_date, cvv)
print("Test Case 1 Passed!")




''' Negative test cases '''

print("\n\nDetails provided for negative test case 1:-\n")          # Card Not present
try:
    card_number="0123-4567-8901-2345"
    cust_name="Debayan Sen"
    exp_date="08/25"
    cvv=274
    
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
        
        
        
print("\n\nDetails provided for negative test case 2:-\n")          # Name does Not match
try:
    card_number="7437-8982-1769-4881"
    cust_name="James Bond"
    exp_date="08/25"
    cvv=274
    
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
    
    
    
print("\n\nDetails provided for negative test case 3:-\n")          # Expiry Date does not match
try:
    card_number="7437-8982-1769-4881"
    cust_name="Debayan Sen"
    exp_date="09/28"
    cvv=274
    
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
    
    

print("\n\nDetails provided for negative test case 4:-\n")          # Card is expired
try:
    card_number="5555-6666-7777-8888"
    cust_name="Anwesa Roy"
    exp_date="04/98"
    cvv=123
    
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
    


print("\n\nDetails provided for negative test case 5:-\n")          # CVV does not match
try:
    card_number="7437-8982-1769-4881"
    cust_name="Debayan Sen"
    exp_date="09/28"
    cvv=287
    
    
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


                     

print("\n\nDetails provided for negative test case 6:-\n")          # Card is inactive
try:
    card_number="8343-6287-1121-4081"
    cust_name="Arumoy Chakraborty"
    exp_date="11/15"
    cvv=946
    
    
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

    
    
           