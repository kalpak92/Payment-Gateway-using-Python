'''
Created on Sep 24, 2015

@author: swayam.sarkar
'''


from utility import DBConnectivity
from classes.Operator_Module import Operator
from classes.Customer_Mobile_Module import customer_mobile
from classes.Aircel_Mobile_Module import Aircel_Mobile
from classes.Airtel_Mobile_Module import Airtel_Mobile
from classes.BSNL_Mobile_Module import BSNL_Mobile
from classes.Idea_Mobile_Module import Idea_Mobile
from classes.Reliance_Mobile_Module import Reliance_Mobile
from classes.Tata_Docomo_Mobile_Module import Tata_Docomo_Mobile
from classes.Tata_Indicom_Mobile_Module import Tata_Indicom_Mobile
from classes.Vodafone_Mobile_Module import Vodafone_Mobile


'''
Retrieves operators belonging to the given operator
'''
def get_operator(operator):
    try:
        count=[];
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select op_name from operator where upper(op_name)=:op_nm and upper(op_id) like 'M%'",{"op_nm":operator.upper()})
        for name in cur:
            operator=Operator();
            operator.set_op_name(name)
            count.append(operator)
        return count;   #Returning a list of operator names
    
    
    finally:
        cur.close()
        con.commit()
        con.close()
 
 
 
'''
Retrieves phone numbers belonging to the given operator and phone number
'''       
def get_phonenoinoperator(phone_no,operator):
    try:
        op=operator.upper()
        opid="";
        count=[];
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur2=DBConnectivity.create_cursor(con)
        cur.execute("select op_id from operator where upper(op_name)=:op_name and upper(op_id) like 'M%'",{"op_name":op.upper()})
        for cid in cur:
            
            opid=cid[0]
            
            cur2.execute("select phone_no from customer_mobile where op_id=:op_id and phone_no=:pho",{"op_id":opid.upper(),"pho":phone_no})
            for ph in cur2:
                phone=customer_mobile()
                phone.set_phone_no(ph)
                count.append(phone)
        
        if(len(count)!=0):        
            return count;
        return False     
                
    finally:
        cur.close()
        cur2.close()
        con.commit()
        con.close()




'''
Retrieves connection type of a particular mobile number
'''
def get_conn_type(phone_no):
    try:
        conn_list=[]
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select conn_type from customer_mobile where phone_no=:ph_no",{"ph_no":phone_no})
        for counter in cur:
            ctype=customer_mobile()
            ctype.set_conn_type(counter)
            conn_list.append(ctype)
            
        if(len(conn_list)!=0):
            return(conn_list[0].get_conn_type())[0];
        return False
    
    
    finally:
        cur.close()
        con.commit()
        con.close()




'''
Retrieves existing balance for given mobile number
'''     
def get_balance(phone_no):
    try:
        balance=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select mob_balance from customer_mobile where phone_no=:ph_no",{"ph_no":phone_no})
        for bal in cur:
            balance=bal[0];
        
        return balance;
    
    finally:
        cur.close()
        con.commit()
        con.close()



'''
Retrieves Recharge Type for a particular amount and operator
'''
def get_plan(amount,operator):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        rechargetype=[]   
        
        if operator.upper()=="IDEA":
            cur.execute("select rech_type from Idea_Mobile where rech_amount=:amt", {"amt":amount}) 
            for rech_type in cur:
                    air=Idea_Mobile()
                    air.set_rech_type(rech_type)
                    rechargetype.append(air)
            if len(rechargetype)!=0 :
                return (rechargetype[0].get_rech_type())[0]
            return False
        
        
        if operator.upper()=="AIRTEL":
            cur.execute("select rech_type from Airtel_Mobile where rech_amount=:amt", {"amt":amount}) 
            for rech_type in cur:
                    air=Airtel_Mobile()
                    air.set_rech_type(rech_type)
                    rechargetype.append(air)
            if len(rechargetype)!=0 :
                return (rechargetype[0].get_rech_type())[0]
            return False
        
        
        if operator.upper()=="AIRCEL":
            cur.execute("select rech_type from Aircel_Mobile where rech_amount=:amt", {"amt":amount}) 
            for rech_type in cur:
                    air=Aircel_Mobile()
                    air.set_rech_type(rech_type)
                    rechargetype.append(air)
            if len(rechargetype)!=0 :
                return (rechargetype[0].get_rech_type())[0]
            return False
        
        
        if operator.upper()=="TATA_INDICOM":
            cur.execute("select rech_type from Tata_Indicom_Mobile where rech_amount=:amt", {"amt":amount}) 
            for rech_type in cur:
                    air=Tata_Indicom_Mobile()
                    air.set_rech_type(rech_type)
                    rechargetype.append(air)
            if len(rechargetype)!=0 :
                return (rechargetype[0].get_rech_type())[0]
            return False
        
        
        if operator=="RELIANCE":
            cur.execute("select rech_type from Reliance_Mobile where rech_amount=:amt", {"amt":amount}) 
            for rech_type in cur:
                    air=Reliance_Mobile()
                    air.set_rech_type(rech_type)
                    rechargetype.append(air)
            if len(rechargetype)!=0 :
                return (rechargetype[0].get_rech_type())[0]
            return False
        
        
        if operator=="TATA_DOCOMO":
            cur.execute("select rech_type from Tata_Docomo_Mobile where rech_amount=:amt", {"amt":amount}) 
            for rech_type in cur:
                    air=Tata_Docomo_Mobile()
                    air.set_rech_type(rech_type)
                    rechargetype.append(air)
            if len(rechargetype)!=0 :
                return (rechargetype[0].get_rech_type())[0]
            return False
        
        
        if operator=="BSNL":
            cur.execute("select rech_type from BSNL_Mobile where rech_amount=:amt", {"amt":amount}) 
            for rech_type in cur:
                    air=BSNL_Mobile()
                    air.set_rech_type(rech_type)
                    rechargetype.append(air)
            if len(rechargetype)!=0 :
                return (rechargetype[0].get_rech_type())[0]
            return False
        
        
        if operator=="VODAFONE":
            cur.execute("select rech_type from Vodafone_Mobile where rech_amount=:amt", {"amt":amount}) 
            for rech_type in cur:
                    air=Vodafone_Mobile() 
                    air.set_rech_type(rech_type)
                    rechargetype.append(air)
            if len(rechargetype)!=0 :
                return (rechargetype[0].get_rech_type())[0]
            return False
        
        
    finally:
            cur.close()
            con.commit()
            con.close()



'''
This function is used for updating the balance in the database
'''
def update_balance(phone_no, amount):
    try:
        con=DBConnectivity.create_connection()
        cur5=DBConnectivity.create_cursor(con)  
        cur5.execute("update customer_mobile set mob_balance =:amt where phone_no = :mob_no",{"mob_no":phone_no,"amt":amount})    
        
        
    finally:
        cur5.close()
        con.commit()
        con.close()
        
        
        
        
