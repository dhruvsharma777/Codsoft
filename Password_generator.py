#Password Generator

import random
a=int(input("Enter the length of your password:"))
f="1234567890@$#!%&*+"
b=''
if(a<3):
    for i in range(a):
        e=random.randint(97,122) #(a-z) #To avoid the characters which allowed as an password
        b+=chr(e)
        
   
    
elif(len(b)<a):
    for i in range(0,2*a,3):
        number=random.randint(65,90)    #(A-Z)
        e=random.randint(97,122) #(a-z) #To avoid the characters which allowed as an password
        b+=chr(e)
        b+=random.choice(f)
        b=b+chr(number)
d=''
for i in range(0,a):
    d+=b[i]
    
print(d)
