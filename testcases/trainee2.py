'''
Created on Sep 25, 2015

@author: athira.soman
'''

from validations.Prepaid_Validations import validate_mobile_number
from exceptions.Prepaid_Exceptions import InvalidMobileNumberException,InvalidOperatorException,InvalidTypeException,InvalidMobileOperatorException

'''positive test cases'''

print("Positive Test Case ::","8723461749 ::","IDEA ::","100 ::","Expected Result - True ::",validate_mobile_number('8723461749','IDEA','100'))
print("\nPositive Test Case ::","8882432001 ::","bsnl ::","78 ::","Expected Result - True ::",validate_mobile_number('8882432001','bsnl','78'))
print("\nPositive Test Case ::","9099942785 ::","Reliance ::","53 ::","Expected Result - True ::",validate_mobile_number('9099942785','Reliance','53'))


'''negative test cases'''

try:

    print("Negative Test Case ::","888243200 ::","idea ::","100 ::","Expected Result - ** INVALID MOBILE NUMBER")
    validate_mobile_number('888243200','idea','100')
except InvalidMobileNumberException as e:
    print(e)
finally:
    print("Negative Test Case for Invalid Mobile Number\n")
    
try:
    print("Negative Test Case ::","9633214560 ::","idea ::","100 ::","Expected Result - ** INVALID MOBILE NUMBER")
    validate_mobile_number('9633612296','idea','100')
except InvalidMobileNumberException as e:
    print (e)
finally:
    print("Negative Test Case for Invalid Mobile Number\n")
    
try:
    print("Negative Test Case ::","8882432001 ::",'uninor ::',"100 ::","Expected Result - ** INVALID OPERATOR")
    validate_mobile_number('8882432001','uninor','100')
except InvalidOperatorException as e:
    print (e)
finally:
    print("Negative Test Case for Invalid Operator\n")
    
try:
    print("Negative Test Case ::","9244307877 ::","vodafone ::","100 ::","Expected Result - ** CANNOT RECHARGE POSTPAID MOBILE")
    validate_mobile_number('9244307877','vodafone','100')
except InvalidTypeException as e:
    print (e)
finally:
    print("Negative Test Case for Invalid Connection Type\n")
    
try:
    print("Negative Test Case::","9392164353,vodafone,100","Expected Result - ** MOBILE NUMBER IS NOT PRESENT IN OPERATOR LIST")
    validate_mobile_number('9392164353','vodafone','100')
except InvalidMobileOperatorException as e:
    print (e)
finally:
    print("Negative Test Case for Invalid Operator against Mobile\n")