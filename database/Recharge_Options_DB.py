'''
Created on Sep 26, 2015
@author: swayam.sarkar
'''


from utility import DBConnectivity
from classes.Operator_Module import Operator
from classes.Aircel_Mobile_Module import Aircel_Mobile
from classes.Airtel_Mobile_Module import Airtel_Mobile
from classes.BSNL_Mobile_Module import BSNL_Mobile
from classes.Idea_Mobile_Module import Idea_Mobile
from classes.Reliance_Mobile_Module import Reliance_Mobile
from classes.Tata_Docomo_Mobile_Module import Tata_Docomo_Mobile
from classes.Tata_Indicom_Mobile_Module import Tata_Indicom_Mobile
from classes.Vodafone_Mobile_Module import Vodafone_Mobile


'''
This function checks whether the customer has provided a valid mobile operator
'''
def get_operator(operator):
    try:
        count=[];
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select op_name from operator where op_name=:op_nm",{"op_nm":operator.upper()})
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
This function retrieves the recharge plan of the specific operator based on the recharge type(s) and range
'''
def get_plans(operator, recharge_type,price_range):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_plans=[]
        if operator.upper()=='AIRTEL':
            if price_range!='':
                price_list=price_range.split('-')
                
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');  
                    for count in list_of_types:
                        
                        cur.execute("select rech_type,rech_amount,scheme,validity from Airtel_Mobile where rech_type='"+count.upper()+"' and rech_amount between "+price_list[0]+" and "+price_list[1])#,{"rech_typ":count,"upper":price_list[1],"lower":price_list[0]})
                        
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Airtel_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                
                else: 
                    cur.execute("select rech_type,rech_amount,scheme,validity from Airtel_Mobile where rech_amount between "+price_list[0]+" and "+price_list[1])#between :upper and :lower",{"upper":price_list[1],"lower":price_list[0]})
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Airtel_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
           
            else:
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');              
                    for count in list_of_types:
                        cur.execute("select rech_type,rech_amount,scheme,validity from Airtel_Mobile where rech_type='" +count.upper()+ "'")         
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Airtel_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else:
                    cur.execute("select rech_type,rech_amount,scheme,validity from Airtel_Mobile")
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Airtel_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
        
        elif operator.upper()=='AIRCEL':
            if price_range!='':
                price_list=price_range.split('-')
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');  
                    for count in list_of_types:
                        
                        cur.execute("select rech_type,rech_amount,scheme,validity from Aircel_Mobile where rech_type='"+count.upper()+"' and rech_amount between "+price_list[0]+" and "+price_list[1])#,{"rech_typ":count,"upper":price_list[1],"lower":price_list[0]})
                        
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Aircel_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else: 
                    cur.execute("select rech_type,rech_amount,scheme,validity from Aircel_Mobile where rech_amount between "+price_list[0]+" and "+price_list[1])#between :upper and :lower",{"upper":price_list[1],"lower":price_list[0]})
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Aircel_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
            else:
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');              
                    for count in list_of_types:
                        cur.execute("select rech_type,rech_amount,scheme,validity from Aircel_Mobile where rech_type='" +count.upper()+ "'")         
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Aircel_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else:
                    cur.execute("select rech_type,rech_amount,scheme,validity from Aircel_Mobile")
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Aircel_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
        
        
        elif operator.upper()=='IDEA':
            if price_range!='':
                price_list=price_range.split('-')
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');  
                    for count in list_of_types:
                        
                        cur.execute("select rech_type,rech_amount,scheme,validity from Idea_Mobile where rech_type='"+count.upper()+"' and rech_amount between "+price_list[0]+" and "+price_list[1])#,{"rech_typ":count,"upper":price_list[1],"lower":price_list[0]})
                        
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Idea_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else: 
                    cur.execute("select rech_type,rech_amount,scheme,validity from Idea_Mobile where rech_amount between "+price_list[0]+" and "+price_list[1])#between :upper and :lower",{"upper":price_list[1],"lower":price_list[0]})
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Idea_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
            else:
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');              
                    for count in list_of_types:
                        cur.execute("select rech_type,rech_amount,scheme,validity from Idea_Mobile where rech_type='" +count.upper()+ "'")         
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Idea_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else:
                    cur.execute("select rech_type,rech_amount,scheme,validity from Idea_Mobile")
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Idea_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
        
        
        elif operator.upper()=='BSNL':
            if price_range!='':
                price_list=price_range.split('-')
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');  
                    for count in list_of_types:
                        
                        cur.execute("select rech_type,rech_amount,scheme,validity from BSNL_Mobile where rech_type='"+count.upper()+"' and rech_amount between "+price_list[0]+" and "+price_list[1])#,{"rech_typ":count,"upper":price_list[1],"lower":price_list[0]})
                        
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=BSNL_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else: 
                    cur.execute("select rech_type,rech_amount,scheme,validity from BSNL_Mobile where rech_amount between "+price_list[0]+" and "+price_list[1])#between :upper and :lower",{"upper":price_list[1],"lower":price_list[0]})
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=BSNL_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
            else:
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');              
                    for count in list_of_types:
                        cur.execute("select rech_type,rech_amount,scheme,validity from BSNL_Mobile where rech_type='" +count.upper()+ "'")         
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=BSNL_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else:
                    cur.execute("select rech_type,rech_amount,scheme,validity from BSNL_Mobile")
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=BSNL_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
        
        
        elif operator.upper()=='VODAFONE':
            if price_range!='':
                price_list=price_range.split('-')
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');  
                    for count in list_of_types:
                        
                        cur.execute("select rech_type,rech_amount,scheme,validity from Vodafone_Mobile where rech_type='"+count.upper()+"' and rech_amount between "+price_list[0]+" and "+price_list[1])#,{"rech_typ":count,"upper":price_list[1],"lower":price_list[0]})
                        
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Vodafone_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else: 
                    cur.execute("select rech_type,rech_amount,scheme,validity from Vodafone_Mobile where rech_amount between "+price_list[0]+" and "+price_list[1])#between :upper and :lower",{"upper":price_list[1],"lower":price_list[0]})
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Vodafone_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
            else:
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');              
                    for count in list_of_types:
                        cur.execute("select rech_type,rech_amount,scheme,validity from Vodafone_Mobile where rech_type='" +count.upper()+ "'")         
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Vodafone_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else:
                    cur.execute("select rech_type,rech_amount,scheme,validity from Vodafone_Mobile")
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Vodafone_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
        
        
        elif operator.upper()=='RELIANCE':
            if price_range!='':
                price_list=price_range.split('-')
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');  
                    for count in list_of_types:
                        
                        cur.execute("select rech_type,rech_amount,scheme,validity from Reliance_Mobile where rech_type='"+count.upper()+"' and rech_amount between "+price_list[0]+" and "+price_list[1])#,{"rech_typ":count,"upper":price_list[1],"lower":price_list[0]})
                        
                        for rech_type,rech_amount,scheme,validity in cur:
                            print(rech_type,rech_amount)
                            airtelob=Reliance_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else: 
                    cur.execute("select rech_type,rech_amount,scheme,validity from Reliance_Mobile where rech_amount between "+price_list[0]+" and "+price_list[1])#between :upper and :lower",{"upper":price_list[1],"lower":price_list[0]})
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Reliance_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
            else:
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');              
                    for count in list_of_types:
                        cur.execute("select rech_type,rech_amount,scheme,validity from Reliance_Mobile where rech_type='" +count.upper()+ "'")         
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Reliance_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else:
                    cur.execute("select rech_type,rech_amount,scheme,validity from Reliance_Mobile")
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Reliance_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
        
        
        elif operator.upper()=='TATA INDOCOM':
            if price_range!='':
                price_list=price_range.split('-')
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');  
                    for count in list_of_types:
                        
                        cur.execute("select rech_type,rech_amount,scheme,validity from Tata_Indicom_Mobile where rech_type='"+count.upper()+"' and rech_amount between "+price_list[0]+" and "+price_list[1])#,{"rech_typ":count,"upper":price_list[1],"lower":price_list[0]})
                        
                        for rech_type,rech_amount,scheme,validity in cur:
                            print(rech_type,rech_amount)
                            airtelob=Tata_Indicom_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else: 
                    cur.execute("select rech_type,rech_amount,scheme,validity from Tata_Indicom_Mobile where rech_amount between "+price_list[0]+" and "+price_list[1])#between :upper and :lower",{"upper":price_list[1],"lower":price_list[0]})
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Tata_Indicom_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
            else:
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');              
                    for count in list_of_types:
                        cur.execute("select rech_type,rech_amount,scheme,validity from Tata_Indicom_Mobile where rech_type='" +count.upper()+ "'")         
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Tata_Indicom_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else:
                    cur.execute("select rech_type,rech_amount,scheme,validity from Tata_Indicom_Mobile")
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Tata_Indicom_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
        
        
        if operator.upper()=='TATA DOCOMO':
            if price_range!='':
                price_list=price_range.split('-')
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');  
                    for count in list_of_types:
                        
                        cur.execute("select rech_type,rech_amount,scheme,validity from Tata_Docomo_Mobile where rech_type='"+count.upper()+"' and rech_amount between "+price_list[0]+" and "+price_list[1])#,{"rech_typ":count,"upper":price_list[1],"lower":price_list[0]})
                        
                        for rech_type,rech_amount,scheme,validity in cur:
                            print(rech_type,rech_amount)
                            airtelob=Tata_Docomo_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else: 
                    cur.execute("select rech_type,rech_amount,scheme,validity from Tata_Docomo_Mobile where rech_amount between "+price_list[0]+" and "+price_list[1])#between :upper and :lower",{"upper":price_list[1],"lower":price_list[0]})
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Tata_Docomo_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
            else:
                if recharge_type!='':
                    list_of_types=recharge_type.split(',');              
                    for count in list_of_types:
                        cur.execute("select rech_type,rech_amount,scheme,validity from Tata_Docomo_Mobile where rech_type='" +count.upper()+ "'")         
                        for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Tata_Docomo_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans
                else:
                    cur.execute("select rech_type,rech_amount,scheme,validity from Tata_Docomo_Mobile")
                    for rech_type,rech_amount,scheme,validity in cur:
                            airtelob=Tata_Docomo_Mobile()
                            airtelob.set_rech_type(rech_type)
                            airtelob.set_rech_amount(rech_amount)
                            airtelob.set_scheme(scheme)
                            airtelob.set_validity(validity)
                            list_of_plans.append(airtelob)
                    return list_of_plans


    finally:
        cur.close()
        con.commit()
        con.close()





        