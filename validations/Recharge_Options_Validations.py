'''
Created on Sep 25, 2015

@author: athira.soman
'''

from exceptions.Recharge_Options_Exceptions import InvalidOperatorException,InvalidRangeException,InvalidRechargeTypeException,NoRechargeOptionException
from database import Recharge_Options_DB


'''
This function is used to validate the details supplied by the user
'''

def validate_mobile_number(operator, recharge_type,price_range):

    list_of_operator = Recharge_Options_DB.get_operator(operator)
    list_of_plans = Recharge_Options_DB.get_plans(operator, recharge_type,price_range)
   
    
    if(len(list_of_operator)==0): #This function is used to validate the operator
        raise InvalidOperatorException       


    if recharge_type!='':
        list_of_types=recharge_type.split(',');
        for count in list_of_types:
            if count.upper() not in ['BALANCE', 'SMS','DATA']:
                raise InvalidRechargeTypeException
        
        
    if price_range!='':
        price_list=price_range.split('-')
        if not(price_list[0].isdigit() and price_list[1].isdigit()):
            raise InvalidRangeException
        else:
            if  float(price_list[0])>float(price_list[1]):
                raise InvalidRangeException
    
    if len(list_of_plans)==0:
        raise NoRechargeOptionException


    return list_of_plans

