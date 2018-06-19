'''
Created on Sep 28, 2015

@author: Riddhita.Sarcar
'''


from exceptions.DTH_Exceptions import InvalidCustomerIDException, InvalidDTHOperatorException, InvalidPhoneNumberException
from validations.DTH_Validations import validate_recharge

print("Trainee 4 : DTH MODULE")

''' Positive test cases '''
print("Details provided for positive test case 1:-\n")
operator_name='sun direct'
phone_no="9697104087"
acct_id=""
print("Operator Name: ", operator_name)
print("Phone Number: ", phone_no)
print("Expected result : TRUE")
list_of_dth_customers=validate_recharge(operator_name, phone_no, acct_id)
print("Test Case 1 Passed!")


print("Details provided for positive test case 2:-\n")
operator_name='videocon'
phone_no=""
acct_id="A9101"
print("Operator Name: ", operator_name)
print("Account ID: ", acct_id)
print("Expected result : TRUE")
list_of_dth_customers=validate_recharge(operator_name, phone_no, acct_id)
print("Test Case 2 Passed!")





''' Negative test cases '''
print("\n\nDetails provided for negative test case 1:-\n")      # Invalid DTH Operator
operator_name="zen"
phone_no="8626221066"
acct_id=""
print("Operator Name: ", operator_name)
print("Phone Number: ", phone_no)
print("Expected result : InvalidDTHOperatorException")
try:
    list_of_dth_customers=validate_recharge(operator_name, phone_no, acct_id)

except InvalidCustomerIDException as e:
    print(e)
    
except InvalidDTHOperatorException as e:
    print(e)
    
except InvalidPhoneNumberException as e:
    print(e)
       
except Exception as e:
    print(e)


print("\n\nDetails provided for negative test case 2:-\n")          # Invalid Customer ID
operator_name='videocon'
phone_no=""
acct_id="A000"
print("Operator Name: ", operator_name)
print("Account ID: ", acct_id)
print("Expected result : InvalidCustomer")
try:
    list_of_dth_customers=validate_recharge(operator_name, phone_no, acct_id)

except InvalidCustomerIDException as e:
    print(e)
    
except InvalidDTHOperatorException as e:
    print(e)
    
except InvalidPhoneNumberException as e:
    print(e)
       
except Exception as e:
    print(e)


print("\n\nDetails provided for negative test case 3:-\n")          # Invalid RMN
operator_name='videocon'
phone_no="9999999999"
acct_id=""
print("Operator Name: ", operator_name)
print("Phone Number: ", phone_no)
print("Expected result : InvalidPhoneNumberException")
try:
    list_of_dth_customers=validate_recharge(operator_name, phone_no, acct_id)

except InvalidCustomerIDException as e:
    print(e)
    
except InvalidDTHOperatorException as e:
    print(e)
    
except InvalidPhoneNumberException as e:
    print(e)
       
except Exception as e:
    print(e)


