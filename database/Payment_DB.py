'''
Created on Sep 26, 2015

@author: Riddhita.Sarcar
'''

from utility import DBConnectivity
from classes.Card_Details_Module import Card_Details
import math
import random


''' 
This function checks whether the card number is present in the database or not
'''
def get_card_number(card_number):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT CARD_NUMBER FROM CARD_DETAILS WHERE CARD_NUMBER=:card_no",{"card_no":card_number})
        
        list_of_card_numbers=[]
        
        for x in cur:
            c_obj=Card_Details()
            c_obj.set_card_number(x[0])
            list_of_card_numbers.append(c_obj)
            
        return list_of_card_numbers
            
    finally:
        cur.close()
        con.commit()
        con.close()
        
        

'''
This function checks whether the customer name is valid or not
'''
def get_customer_name(customer_name, card_number):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT CUST_NAME FROM CARD_DETAILS WHERE CARD_NUMBER=:card_no AND UPPER(CUST_NAME)=:cust_name",{"card_no":card_number, "cust_name":customer_name.upper()})
        
        list_of_customer_names=[]
        
        for x in cur:
            c_obj=Card_Details()
            c_obj.set_cust_name(x[0])
            list_of_customer_names.append(c_obj)
            
        return list_of_customer_names
            
    finally:
        cur.close()
        con.commit()
        con.close()
        
        
             
'''
This function checks whether the expiry date is valid or not
'''
def get_expiry_dates(expiry_date, card_number):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT EXPIRY_DATE FROM CARD_DETAILS WHERE CARD_NUMBER=:card_no AND EXPIRY_DATE=:exp_date",{"card_no":card_number, "exp_date":expiry_date})
        
        list_of_expiry_dates=[]
        
        for x in cur:
            c_obj=Card_Details()
            c_obj.set_expiry_date(x[0])
            list_of_expiry_dates.append(c_obj)
        
        return list_of_expiry_dates
            
    finally:
        cur.close()
        con.commit()
        con.close()
            
       
    
'''
This function checks whether the card is expired or not
'''
def check_expiry_date(list_of_expiry_date):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        dict_of_months={"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", "06":"Jun", "07":"Jul", "08":"Aug", "09":"Sep", "10":"Oct", "11":"Nov", "12":"Dec"}
        dt=(list_of_expiry_date[0].get_expiry_date()).split("/")
        
        exp_date="01-"+str(dict_of_months[dt[0]])+"-20"+str(dt[1])
        cur.execute("SELECT TO_DATE(:e_date, 'dd-Mon-YYYY')-SYSDATE FROM DUAL", {"e_date":exp_date})
        
        for x in cur:
            x=math.floor(x[0])
        
        
        if x<=0:
            return False
        return True
            
            
    finally:
        cur.close()
        con.commit()
        con.close()
            
    
    
'''
This function checks whether the CVV is valid or not
'''   
def get_cvv(cvv, card_number):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT CVV FROM CARD_DETAILS WHERE CARD_NUMBER=:card_no",{"card_no":card_number})
        
        list_of_cvv=[]
        
        for x in cur:
            c_obj=Card_Details()
            c_obj.set_cvv(x[0])
            list_of_cvv.append(c_obj)
        
        return list_of_cvv
            
    finally:
        cur.close()
        con.commit()
        con.close()
            
       
 
'''
This function checks whether the account is inactive or active
'''     
def check_status(card_number):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT STATUS FROM CARD_DETAILS WHERE CARD_NUMBER=:card_no",{"card_no":card_number})
        
        list_of_status=[]
        
        for x in cur:
            if x[0].lower()=='active':
                c_obj=Card_Details()
                c_obj.set_status(x[0])
                list_of_status.append(c_obj)
        
        return list_of_status

    finally:
        cur.close()
        con.commit()
        con.close()
            
    
'''
This function retrieves the details of the card
'''    
def get_details(card_number):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        cur.execute("SELECT * FROM CARD_DETAILS WHERE CARD_NUMBER=:card_no",{"card_no":card_number})
        
        list_of_details=[]
        
        for a, b, c, d, e, f, g, h in cur:
            c_obj=Card_Details()
            c_obj.set_card_number(a)
            c_obj.set_cust_name(b)
            c_obj.set_expiry_date(c)
            c_obj.set_cvv(d)
            c_obj.set_card_type(e)
            c_obj.set_status(f)
            c_obj.set_balance(g)
            c_obj.set_grid_code(h)
                    
            list_of_details.append(c_obj)
        
        return list_of_details

    finally:
        cur.close()
        con.commit()
        con.close()
    

    
'''
This function generates grid question and the answer
'''   
def generate_grid_question(list_of_details):
    ''' This list contains the grid values '''
    list_of_grid_values=(list_of_details[0].get_grid_code()).split("-")

    
    list_of_alphabets=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    dict_of_grid_values={"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13,"O":14, "P":15}
    
    list_of_index=[]*3
    question_list=[]*3
    answer_list=[]*3
    
    
    while True:
        i=random.randrange(0,16)
        if i not in list_of_index:
            list_of_index.append(i)
        if len(list_of_index)==3:
            break
        
    list_of_index.sort()
    
    for i in range(0, 3):
        question_list.append(list_of_alphabets[list_of_index[i]])
        answer_list.append(list_of_grid_values[int(dict_of_grid_values[question_list[i]])])
        
        
    result=[]
    result.append(question_list[0]+"-"+question_list[1]+"-"+question_list[2])
    result.append(str(answer_list[0])+"-"+str(answer_list[1])+"-"+str(answer_list[2]))

    return result

    

'''
This function signifies the transactional functionality
'''
def transaction(list_of_details, amount):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)

        card_number=list_of_details[0].get_card_number()
        balance=list_of_details[0].get_balance()
        amount=float(amount)
        
        if balance<amount:
            return False
        
        balance-=amount
        cur.execute("UPDATE CARD_DETAILS SET BALANCE=:bal WHERE CARD_NUMBER=:card_no",{"bal":balance, "card_no":card_number})
        
        return True
        
        
    finally:
        cur.close()
        con.commit()
        con.close()  
    
    
    
    
    
    