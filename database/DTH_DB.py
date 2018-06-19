'''
Created on Sep 24, 2015

@author: Riddhita.Sarcar
'''

from utility import DBConnectivity
from classes.Operator_Module import Operator
from classes.Customer_DTH_Module import Customer_DTH
from exceptions.DTH_Exceptions import InvalidDTHBalanceException 
import math


'''
This function checks whether the customer has provided a valid DTH operator
'''
def get_DTH_Operator(operator_name):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT OP_ID FROM OPERATOR WHERE OP_NAME=:op_name AND OP_ID LIKE 'D%'",{"op_name":operator_name.upper()})
        
        list_of_operators=[]
        
        for o_id in cur:
            operator_obj=Operator()
            operator_obj.set_op_id(o_id[0])
            list_of_operators.append(operator_obj)
            
        return list_of_operators
            
    finally:
        cur.close()
        con.commit()
        con.close()
      


'''
This function is used to retrieve the corresponding Account ID
'''
def get_Account_ID(acct_id, operator_id):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT ACCOUNT_ID FROM CUSTOMER_DTH WHERE ACCOUNT_ID=:acc_id AND OP_ID=:op_id",{"acc_id":acct_id.upper(), "op_id":operator_id.upper()})
        
        list_of_account_ids=[]
        
        for a_id in cur:
            customer_obj=Customer_DTH()
            customer_obj.set_account_id(a_id[0])
            list_of_account_ids.append(customer_obj)
        
        return list_of_account_ids
            
    finally:
        cur.close()
        con.commit()
        con.close()
    
    
  
'''
This function is used to check whether the Phone Number provided by the customer is a registered account or not
'''
def get_RMN(phone_no, operator_id):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT PHONE_NO FROM CUSTOMER_DTH WHERE PHONE_NO=:ph_no AND OP_ID=:op_id",{"ph_no":phone_no, "op_id":operator_id.upper()})
        
        list_of_phone_numbers=[]
        
        for rmn in cur:
            rmn_obj=Customer_DTH()
            rmn_obj.set_phone_no(rmn[0])
            list_of_phone_numbers.append(rmn_obj)
            
        return list_of_phone_numbers
    
    finally:
        cur.close()
        con.commit()
        con.close()
    
   

'''
This function is used to get all the details related to the particular customer
''' 
def get_details(phone_no, acct_no):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        
        cur.execute("SELECT * FROM CUSTOMER_DTH WHERE PHONE_NO=:ph_no OR ACCOUNT_ID=:acc_no",{"ph_no":phone_no, "acc_no":acct_no.upper()})
        
        list_of_details=[]
        
        for account_id, dth_balance, due_date, phone_no, op_id in cur:
            customer_obj=Customer_DTH()
            customer_obj.set_account_id(account_id)
            customer_obj.set_dth_balance(dth_balance)
            dd=str(due_date)
            customer_obj.set_due_date(dd[:10])
            customer_obj.set_phone_no(phone_no)
            customer_obj.set_op_id(op_id)

            list_of_details.append(customer_obj)
        return list_of_details
    
    finally:
        cur.close()
        con.commit()
        con.close()


        
'''
This function is used to check whether the year is a leap year or not
'''   
def isLeapYear(year):
    if(year%400==0):
        return True
    elif(year%4==0):
        if(year%100!=0):
            return True
        else:
            return False
    else:
        return False


        
'''
This function is used to generate the bill
'''
def generate_bill(list_of_details, amount):
    try:
        con=DBConnectivity.create_connection()
        cur1=DBConnectivity.create_cursor(con)
        cur2=DBConnectivity.create_cursor(con)
        
        operator_id=list_of_details[0].get_op_id()
        acct_id=list_of_details[0].get_account_id()
        d_d=str(list_of_details[0].get_due_date())
        due_date=d_d.split("-")
        
        dict_of_months={"1":"Jan", "2":"Feb", "3":"Mar", "4":"Apr", "5":"May", "6":"Jun", "7":"Jul", "8":"Aug", "9":"Sep", "10":"Oct", "11":"Nov", "12":"Dec"}
        list_of_months_30_days=["04", "06", "09", "11"]
        list_of_months_31_days=["01", "03", "05", "07", "08", "10", "12"]
        
        
        cur1.execute("SELECT MONTHLY_RENTAL FROM OPERATOR_DTH WHERE OP_ID=:op_id", {"op_id":operator_id.upper()})
        for x in cur1:
            rent=x[0]
        
        total_balance=list_of_details[0].get_dth_balance()+amount
        n=int(total_balance//rent)

        sp_days=0
        sp_months=0
        
        if n<3:
            sp_days=0
            sp_months=1
        elif n>=3 and n<6:
            sp_days=4
            sp_months=3
        elif n>6 and n<12:
            sp_days=14
            sp_months=6
        elif n>=12:
            sp_days=30
            sp_months=12
        
        cur2.execute("SELECT DUE_DATE-SYSDATE FROM CUSTOMER_DTH WHERE ACCOUNT_ID=:acc_id", {"acc_id": acct_id.upper()})
        x=0
        for x in cur2:
            x=int(math.floor(x[0]))
          
            
        new_balance=total_balance-(rent*sp_months)
        if new_balance<0:
            raise InvalidDTHBalanceException 
        else:
            new_balance=round(new_balance, 2)
            
            if x>=7 and x<=16:
                new_balance=new_balance+amount*0.07
            
            list_of_details[0].set_dth_balance(abs(new_balance))
        
        '''
        Calculation of Due Date
        '''
        
        no_of_days=30
        if due_date[1] in list_of_months_30_days:
            no_of_days=30
        elif due_date[1] in list_of_months_31_days:
            no_of_days=31
        else:
            if isLeapYear(due_date[0]):
                no_of_days=29
            else:
                no_of_days=28
        
        d=int(due_date[2])
        m=int(due_date[1])
        y=int(due_date[0])
            
        d+=sp_days  
        if d>no_of_days:
            d-=no_of_days
            m+=1
        
        m+=sp_months
        if m>12:
            m-=12
            y+=1
        
        new_due_date=str(d)+"-"+dict_of_months[str(m)]+"-"+str(y)
        cur2.execute("UPDATE CUSTOMER_DTH SET DTH_BALANCE=:new_bal, DUE_DATE=:d_date",{"new_bal":abs(new_balance), "d_date":new_due_date})
        
        return list_of_details
      
        
    finally:
        cur1.close()
        cur2.close()
        con.commit()
        con.close()
        
        
        
    