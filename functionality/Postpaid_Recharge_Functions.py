'''
Created on Sep 24, 2015

@author: Kalpak.Seal
'''


from exceptions.Postpaid_Exceptions import InvalidMobileNumberException, InvalidOperatorException, InvalidAmountException, MobileDoesNotBelongToOperatorException, InvalidMobileTypeException
from functionality.GenerateCaptcha import *
from functionality.Payment_Functions import *
from functionality.DTH_Functions import *
from database import Postpaid_DB
from validations import Postpaid_Validations 


'''
This function is used for Bill Payment
'''
def postpaid_bill_payment():
    flag=False
    
    try:
                
        mobile_no = input("Enter Mobile No: ")
        operator = input("Enter your operator: ")
        amount = input("Enter the amount: ")
         
                
        if Postpaid_Validations.validate_mobile_number(mobile_no, operator, amount):
            answer = generate_random() 
            ans= input("Answer: ")
                
            if(int(ans) == answer):
                flag=True
                balance=Postpaid_DB.get_balance(mobile_no)
                outstanding=balance-float(amount)
                    
                status=payment(amount)
                    
                if status:
                        print("Payment Successful. Your Outstanding Amount is:"+ str(outstanding))
                        Postpaid_DB.update_balance(mobile_no,outstanding)
                        
                        choice = input("Do you wish to Pay bill/Recharge DTH or quit (B/D/N): ") 
                        if(choice.upper() == "B"):
                            postpaid_bill_payment()
                        elif(choice.upper() == "D"):
                            DTH_Recharge()
                        elif(choice.upper() == "N"):
                            pass
                        else:
                            print("Enter a valid choice.")     
            else: 
                print("Wrong answer!")
                
                        
                        
                
            
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
        
   
   
    
    finally:
        if not(flag):
            new_choice=input("Do you wish to continue (Y/N)? ")
            
            if new_choice.upper()=='Y':
                postpaid_bill_payment()
    
            elif new_choice.upper()=='N':
                pass
                
            else:
                print("Enter a valid choice.")
 
 
 
 
    
    

