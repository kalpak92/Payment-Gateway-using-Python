'''
Created on Sep 24, 2015

@author: swayam.sarkar
'''


from database import Prepaid_DB
from exceptions.Prepaid_Exceptions import InvalidMobileNumberException, InvalidOperatorException, InvalidMobileOperatorException, InvalidTypeException
from exceptions.Input_Exceptions import InvalidInputException    
from functionality.GenerateCaptcha import *
from functionality.Postpaid_Recharge_Functions import *
from functionality.Payment_Functions import *
from validations.Prepaid_Validations import *


'''
This function is used for Quick Recharge
'''
def quick_recharge(rechargeamt,op):
    flag=False 
    
    try:
        phone_no=input("Mobile Number: ")
        
        if op==None:
            operator=input("Operator: ")
                
        else:
            operator=op
            print("Operator: "+operator)
        
        
        if rechargeamt==None:
            amount=input("Amount: ")
            while float(amount)<0.0:
                amount=input("Amount: ")
        
        else:
            amount=str(float(rechargeamt))
            print("Amount: "+str(round(amount, 2)))
       
       
        if validate_mobile_number(phone_no, operator, amount):
            print("Answer the question: ") 
            answer=generate_random()
            user_answer=input("Answer: ")
            
            if answer==int(user_answer):
                flag=True
                balance=Prepaid_DB.get_balance(phone_no)
                rtype=Prepaid_DB.get_plan(amount, operator)
                
                if(rtype=="BALANCE"):
                    new_balance=balance+float(amount)        
                elif rtype=="DATA":
                    new_balance=balance
                elif rtype=="SMS":
                    new_balance=balance
                else:
                    new_balance=balance+(0.88*float(amount))
                        
                status=payment(amount)
                    
                if status:
                    print("Recharge Successful. Your balance is Rs. "+str(new_balance))   
                    Prepaid_DB.update_balance(phone_no, new_balance)
                    
                    choice=input("Do you wish to recharge/pay bill or quit (R/B/N): ")
                    if choice.upper()=='R':
                        quick_recharge(None,None)                        
                    elif choice.upper()=='B':
                        postpaid_bill_payment()
                    elif choice.upper()=='N':
                        pass                              
                    else:
                        print("Enter a valid choice.")
    
            else:
                print("Wrong answer!")
                
                
                 
    except InvalidMobileNumberException as e:
        print(e)   
        
    except InvalidOperatorException as e:
        print(e) 
        
    except InvalidMobileOperatorException as e: 
        print(e)
        
    except InvalidTypeException as e:
        print(e)
     
        

    finally:
        if not(flag):
            new_choice=input("Do you wish to continue (Y/N)? ")
    
            if new_choice.upper()=='Y':
                quick_recharge(rechargeamt,None)
                
            elif new_choice.upper()=='N':
                pass
                
            else:
                print("Enter a valid choice.")
 
 
 
 

 