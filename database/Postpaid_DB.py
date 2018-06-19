from utility import DBConnectivity

from classes.Customer_Mobile_Module import customer_mobile 
from classes.Operator_Module import Operator


'''
This function checks whether the customer has provided a valid Mobile operator and Mobile number
'''
def get_mobile_in_operator(mobile_no, operator):
    try:
        con=DBConnectivity.create_connection()
        cur1=DBConnectivity.create_cursor(con)
        cur2=DBConnectivity.create_cursor(con)
        list_of_mobile_in_operator=[]
        
        x="0"
        
        cur1.execute("select op_id from operator where upper(op_name)=:op  and upper(op_id) like 'M%'",{"op":operator.upper()})
        
        for i in cur1:
            x = i[0]
        
        cur2.execute("select phone_no from customer_mobile where phone_no=:mob_no and upper(op_id)=:operator_id",{"mob_no":int(mobile_no),"operator_id":x.upper()})
        
        for mobileno in cur2:    
            mobile_no=customer_mobile()                        
            mobile_no.set_phone_no(mobileno)
            
            list_of_mobile_in_operator.append(mobile_no)
        
        return list_of_mobile_in_operator
        
    
    finally:
        cur1.close()
        cur2.close()
        con.commit()
        con.close()


'''
This function checks whether the customer has provided a valid Mobile operator
'''
def get_operator(operator):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_operator=[]
        
        cur.execute("select op_name from operator where upper(op_name)=:op and upper(op_id) like 'M%'",{"op":operator.upper()})
        
        for operatorname in cur:
            operator_name=Operator()
            operator_name.set_op_name(operatorname[0])
            
            list_of_operator.append(operator_name)
            
        return list_of_operator
    
    finally:
        cur.close()
        con.commit()
        con.close()


        
'''
This function is used to verify whether the mobile number is present in the database
'''        
def get_mobile_no( mobile_no):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_mobileno=[]
        
        cur.execute("select phone_no from customer_mobile where phone_no=:ph",{"ph":mobile_no})
        
        for mobileno in cur:
            mob_no=customer_mobile()
            mob_no.set_phone_no(mobileno)

            list_of_mobileno.append(mob_no)
        
        return list_of_mobileno
    
    finally:
        cur.close()
        con.commit()
        con.close()
        
        
        
'''
Retrieves connection type of a particular mobile number
'''
def get_conn_type(mobile_no):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        
        list_of_conn_type=[]
        
        cur.execute("select conn_type from customer_mobile where phone_no=:mob_no",{"mob_no":mobile_no})
        
        for conn_type in cur:
            c_type=customer_mobile()
            c_type.set_conn_type(conn_type)
            
            list_of_conn_type.append(c_type)
        
        return (list_of_conn_type[0].get_conn_type())[0]
    
    finally:
        cur.close()
        con.commit()
        con.close()
        
        
        
'''
Retrieves existing balance for given mobile number
'''              
def get_balance( mobile_no):
    try:
        balance=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
                       
        cur.execute("select mob_balance from customer_mobile where phone_no=:mob_no",{"mob_no":mobile_no})
            
        for bal in cur:
            balance=bal[0]
        
        return float(balance)
        
    finally:
        cur.close()
        con.commit()
        con.close()
            
            
            
'''
This function is used for updating the balance in the database
'''                
def update_balance(mobile_no, amount):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("update customer_mobile set mob_balance =:amt where phone_no = :mob_no",{"mob_no":mobile_no,"amt":amount})
        
        
    finally:
        cur.close()
        con.commit()
        con.close()

        
                         
                