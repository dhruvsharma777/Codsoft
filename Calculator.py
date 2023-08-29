#CALCULATOR 

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=input("Enter a appropriate operator(+,-,*,/) :")
if c=="+":
   d=a+b;
elif c=="-":
   d=a-b;
elif c=="*":
   d=a*b;
elif c=="/":
   d=a/b;
else :
   d="Wrong input";
print (f"Final answer is {d}")
