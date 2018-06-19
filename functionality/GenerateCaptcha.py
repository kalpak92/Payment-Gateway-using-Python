'''
Created on Sep 24, 2015

@author: swayam.sarkar
'''


import random

    
def generate_random():
    op_list=['+','-','*']
    
    a=random.randrange(1,10)
    b=random.randrange(1,10)
    count=random.randrange(0,3)
    
    c=op_list[count]
    output=0
    
    print(str(a)+" "+c+" "+str(b)+" = ?")
    
    
    if count==0:
        output=(a+b)
    elif count==1:
        output=(a-b)
    else:
        output=(a*b)
        
        
    return output

        
