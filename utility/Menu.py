'''
Created on Sep 18, 2015

@author: Krishnendu_C
'''
'''
This module displays a menu to the user.
'''

from functionality.Recharge_Options_Functions import *
from functionality.Prepaid_Recharge_Functions import *
from functionality.Postpaid_Recharge_Functions import *
from functionality.DTH_Functions import *


     
print("+~~~~~~~~~~~~~~~~~~~~~~~~~~+")
print("$ Recharge with PyReCharge $")
print("+~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    
print("Choose an option from below:\n")
    
end=False
    
while(end==False):
    print("1. Recharge Options")
    print("2. Quick Recharge")
    print("3. Bill Payment")
    print("4. DTH Recharge")
    print("5. Quit")
    option=input()
        
    if(option.isdigit() and (int(option)>=1 or int(option)<=5)):
        if(int(option)==1):
            print("PyReCharge Recharge Options:")
            recharge_options() 
           
           
        if(int(option)==2):
            print("PyReCharge Quick Recharge:")
            quick_recharge(None,None)
                
                
        if(int(option)==3):
            print("PyReCharge Bill Payment:")
            postpaid_bill_payment()
                
             
        if(int(option)==4):
            print("PyReCharge DTH Recharge:")
            DTH_Recharge()
                
                
        if(int(option)==5):
            print("Thank you!")
            end=True
                
                
    else:
        print("Please enter a valid option ( 1,2,3,4,5)")


            