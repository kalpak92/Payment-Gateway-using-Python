'''
Created on Sep 28, 2015

@author: Riddhita.Sarcar
'''

from exceptions.Postpaid_Exceptions import *
from validations.Postpaid_Validations import validate_mobile_number

print("Trainee 3 : POSTPAID MODULE")




''' Positive test cases '''

print("Details provided for positive test case 1:-\n")
operator_name='vodafone'
mobile_no="9244307877"
amount="1200"
print("Operator Name: ", operator_name)
print("Phone Number: ", mobile_no)
print("Amount: ", amount)
print("Expected result : TRUE")
list_of_postpaid_customers=validate_mobile_number(mobile_no, operator_name, amount)
print("Test Case 1 Passed!")






''' Negative test cases '''

print("\n\nDetails provided for negative test case 1:-\n")      # InvalidOperatorException
operator_name="zen"
phone_no="8626221066"
amount="1000"
print("Operator Name: ", operator_name)
print("Phone Number: ", phone_no)
print("Amount: ", amount)
print("Expected result : InvalidOperatorException")
try:
    list_of_postpaid_customers=validate_mobile_number(mobile_no, operator_name, amount)
    
except InvalidMobileNumberException as e:
    print(e)
        
except InvalidOperatorException as e:
    print(e)
        
except InvalidAmountException as e:
    print(e)
        
except MobileDoesNotBelongToOperatorException as e:
    print(e)
        
except InvalidMobileTypeException as e:
    print(e)
    


print("\n\nDetails provided for negative test case 2:-\n")      # InvalidMobileDoesNotBelongToOperatorException
operator_name="Idea"
phone_no="7845629654"
amount="2000"
print("Operator Name: ", operator_name)
print("Phone Number: ", phone_no)
print("Amount: ", amount)
print("Expected result : InvalidMobileDoesNotBelongToOperatorException")
try:
    list_of_postpaid_customers=validate_mobile_number(mobile_no, operator_name, amount)
    
except InvalidOperatorException as e:
    print(e)
        
except InvalidAmountException as e:
    print(e)
        
except MobileDoesNotBelongToOperatorException as e:
    print(e)
        
except InvalidMobileTypeException as e:
    print(e)



print("\n\nDetails provided for negative test case 3:-\n")      # Cannot recharge Prepaid mobile
operator_name="airtel"
phone_no="9410720397"
amount="2000"
print("Operator Name: ", operator_name)
print("Phone Number: ", phone_no)
print("Amount: ", amount)
print("Expected result : InvalidMobileTypeException")
try:
    list_of_postpaid_customers=validate_mobile_number(mobile_no, operator_name, amount)
    
except InvalidOperatorException as e:
    print(e)
        
except InvalidAmountException as e:
    print(e)
        
except MobileDoesNotBelongToOperatorException as e:
    print(e)
        
except InvalidMobileTypeException as e:
    print(e)
    
    
    
print("\n\nDetails provided for negative test case 4:-\n")      # Amount lower boundary
operator_name="Reliance"
phone_no="8738359800"
amount="3900"
print("Operator Name: ", operator_name)
print("Phone Number: ", phone_no)
print("Amount: ", amount)
print("Expected result : Amount Exception (Amount is less than 80% of Bill)")
try:
    list_of_postpaid_customers=validate_mobile_number(mobile_no, operator_name, amount)
    
except InvalidOperatorException as e:
    print(e)
        
except InvalidAmountException as e:
    print(e)
        
except MobileDoesNotBelongToOperatorException as e:
    print(e)
        
except InvalidMobileTypeException as e:
    print(e)   
    
    
    
print("\n\nDetails provided for negative test case 4:-\n")      # Amount upper boundary
operator_name="Reliance"
phone_no="8738359800"
amount="5500"
print("Operator Name: ", operator_name)
print("Phone Number: ", phone_no)
print("Amount: ", amount)
print("Expected result : Amount Exception (Amount is greater than 110% of Bill)")
try:
    list_of_postpaid_customers=validate_mobile_number(mobile_no, operator_name, amount)
    
except InvalidOperatorException as e:
    print(e)
        
except InvalidAmountException as e:
    print(e)
        
except MobileDoesNotBelongToOperatorException as e:
    print(e)
        
except InvalidMobileTypeException as e:
    print(e)   
    
    
    
    