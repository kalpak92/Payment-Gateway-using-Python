'''
Created on Sep 28, 2015

@author: swayam.sarkar
'''
from validations.Recharge_Options_Validations import validate_mobile_number
from exceptions.Recharge_Options_Exceptions import InvalidOperatorException,InvalidRangeException,InvalidRechargeTypeException,NoRechargeOptionException

'''
positive test cases
'''
print("Positive Test Case ::","Airtel ::","Balance,SMS,Data ::",'20-300 ::',"Expected Result ::\n1. Rs.110.0 FULL TALKTIME 28 Days\n2. Rs.222.0 FULL TALKTIME 28 Days\n3. Rs.300.0 FULL TALKTIME 28 Days\n4. Rs.26.0 75MB 2G DATA PACK 7 Days\n5. Rs.43.0 60MB 3G DATA PACK 7 Days\n6. Rs.125.0 1GB 2G DATA PACK 28 Days\n7. Rs.251.0 1GB 3G DATA PACK 28 Days\n")
validate_mobile_number('Airtel', 'Balance,SMS,Data', '20-300')

print("Positive Test Case ::","VODAFONE ::","SMS ::",' ::',"Expected Result ::\n1. Rs.22.0 500 NATIONAL SMS PACK 7 Days\n2. Rs.110.0 1000 NATIONAL SMS PACK 21 Days\n")
validate_mobile_number('VODAFONE', 'SMS', '')

print("Positive Test Case ::","BSNL ::"," ::"," ::","Expected Result ::\n1. Rs.200.0 FULL TALKTIME 30 Days\n2. Rs.78.0 450MB 2G/3G DATA PACK 12 Days\n3. Rs.17.0 90MB 2G/3G DATA PACK 2 Days\n4. Rs.26.0 FULL TALKTIME 4 Days\n5. Rs.251.0 2.2GB 2G/3G DATA PACK 28 Days\n6. Rs.53.0 860 NATIONAL SMS PACK 30 Days\n7. Rs.110.0 FULL TALKTIME 30 Days\n8. Rs.83.0 1650 NATIONAL SMS PACK 30 Days\n9. Rs.13.0 130 NATIONAL SMS 7 Days\n")
validate_mobile_number('BSNL', '', '')

'''
invalid operator
'''
try:
    print("Negative Test Case ::",'Uninor ::', 'Balance,SMS,Data ::' , '30-500 ::',"Expected Result :: ** INVALID OPERATOR")
    list_of_plans=validate_mobile_number('Uninor', 'Balance,SMS,Data' , '30-500')
except InvalidOperatorException as e:
        print(e)
finally:
    print("Negative Test Case for Invalid Operator\n")

'''
invalid recharge type
'''    
try:
    print("Negative Test Case ::",'Airtel ::', 'Talktime,SMS,Data ::' , ' ::',"Expected Result :: ** INVALID RECHARGE TYPE")
    list_of_plans=validate_mobile_number('Airtel', 'Talktime,SMS,Data' , '')
except InvalidRechargeTypeException as e:
        print(e)       
finally:
    print("Negative Test Case for Invalid Recharge Type\n")
    

'''
invalid range
'''
try:
    print("Negative Test Case ::",'Tata Docomo ::', ' ::' , ' 500-30::',"Expected Result :: ** INVALID RANGE")
    list_of_plans=validate_mobile_number('Tata Docomo', '' , '500-30') 
except InvalidRangeException as e:
        print(e) 
finally:
    print("Negative Test Case for Invalid Range\n")
    
'''
No Recharge option (Boundary Value Check)
'''
try:
    print("Negative Test Case ::",'bsnl ::', ' ::' , ' 0-12::',"Expected Result :: ** NO RECHARGE OPTION")
    list_of_plans=validate_mobile_number('bsnl', '' , '0-12')
except NoRechargeOptionException as e:
        print(e)
finally:
    print("Negative Test Case for No Recharge Option Available\n")
    
'''
No Recharge option (Boundary Value Check)
'''
try:
    print("Negative Test Case ::",'airtel ::', ' balance::' , ' 301-500::',"Expected Result :: ** NO RECHARGE OPTION")
    list_of_plans=validate_mobile_number('airtel', 'balance' , '301-500')
except NoRechargeOptionException as e:
        print(e)
finally:
    print("Negative Test Case for No Recharge Option Available\n")

