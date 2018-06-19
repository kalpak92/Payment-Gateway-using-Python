'''
Created on Sep 24, 2015

@author: Riddhita.Sarcar
'''


from database import DTH_DB
from exceptions.DTH_Exceptions import InvalidAmountException, InvalidCustomerIDException, InvalidDTHBalanceException, InvalidDTHOperatorException, InvalidPhoneNumberException
from functionality.Postpaid_Recharge_Functions import *
from functionality.Payment_Functions import *
from validations import DTH_Validations
from exceptions.Input_Exceptions import InvalidInputException



def DTH_Recharge():
    flag=False
    
    try:
        operator_name=input("DTH Provider: ")
        u_id=input("Customer Id/Registered Mobile Number: ")
        amount=int(input("Amount: "))
        
        phone_no=""
        acct_id=""
        
        if len(u_id)==10:
            phone_no=u_id
            
        else:
            acct_id=u_id

        #o_n=operator_name.replace(" ", "")
        
        #if o_n.isalpha() and u_id.isdigit() and amount.isdigit():
        #    pass
        #else:
        #    raise InvalidInputException
        
        list_of_customer_details=DTH_Validations.validate_recharge(operator_name, phone_no, acct_id)
        
        
        status=payment(amount)
        
        if status:
            flag=True
            list_of_customer_details=DTH_DB.generate_bill(list_of_customer_details, amount)
            print("Recharge successful.")
            print("Your Account "+list_of_customer_details[0].get_account_id()+" balance is Rs. "+str(list_of_customer_details[0].get_dth_balance())+".")
            
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
            print("Recharge Unsuccesful.")
            
            
            
        
    except InvalidAmountException as e:
        print(e)
    
    except InvalidCustomerIDException as e:
        print(e)
    
    except InvalidDTHOperatorException as e:
        print(e)
    
    except InvalidPhoneNumberException as e:
        print(e)
    
    except InvalidDTHBalanceException as e:
        print(e)
    
    #except InvalidInputException as e:
    #    print(e)
        
        
    finally:
        if not(flag):
            new_choice=input("Do you wish to continue (Y/N)? ")
            
            if new_choice.upper()=='Y':
                DTH_Recharge()
    
            elif new_choice.upper()=='N':
                pass
                
            else:
                print("Enter a valid choice.")
 
        
        