'''
Created on Sep 24, 2015

@author: athira.soman
'''

from exceptions.Recharge_Options_Exceptions import InvalidOperatorException,InvalidRangeException,InvalidRechargeTypeException,NoRechargeOptionException
from functionality.Prepaid_Recharge_Functions import *
from validations.Recharge_Options_Validations import *


'''
This function is used for displaying the Recharge Options
'''
def recharge_options(): 
    flag=False
        
    try:
        operator=input("Operator: ")
        recharge_type=input("Recharge Type (Optional): ")
        price_range=input("Price Range (Optional): ")
        
        recharge_type="".join(recharge_type.split())
        
        price_range="".join(price_range.split())
                
                
                
        list_of_plans=validate_mobile_number(operator, recharge_type,price_range)
        
        
         
        if (list_of_plans):
            flag=True
            print("\nWallaah! Your recharge options are here: ")
            counter=len(list_of_plans)
    
            for i in range(0,counter):
                print(str(i+1)+"."+" Rs."+str(list_of_plans[i].get_rech_amount())+" "+list_of_plans[i].get_scheme()+" "+str(list_of_plans[i].get_validity())+" Days")
    
            
            recharge_choice=input("Do you wish to Recharge (Y/N)? ")
            if recharge_choice.upper()=='Y':
                choice=int(input("Recharge Option: "))
                choice=choice-1;
                
                if choice in range(0,counter):
                    flag=True
                    rechargeamt=list_of_plans[choice].get_rech_amount()
                    quick_recharge(rechargeamt,operator)
                         
            elif recharge_choice.upper()=='N':
                pass
            
            else:
                print("Enter a valid choice.")
            
        
        
        
    except InvalidRechargeTypeException as e:
        print(e)
        
    except InvalidOperatorException as e:
        print(e)
        
    except NoRechargeOptionException as e:
        print(e)
        
    except InvalidRangeException as e:
        print(e)
    
    
    finally:
        if not(flag):
            new_choice=input("Do you wish to continue (Y/N)? ")
            
            if new_choice.upper()=='Y':
                recharge_options()
            
            elif new_choice.upper()=='N':
                pass
            
            else:
                print("Enter a valid choice.")
                
                
                
                
                

