#password verifier
#mr x is trying to create a new password for his instagram account these are the required conditions for creating a new password
#1:minimum length is 8 max is 
#2:only@,# is allowed in a password
#3:rno spaces are allowed
#4:only alpha numerics are allowed
#you are supposed to print weak if length is exact 8.12,strong if length is b/w 12.15

x=input("enter the password:")
n=len(x)
str="a/"
for a in x:
  if((n<=8)) :
   print("weak",end=" ")   
  elif(8<n<15 ):
   print("strong",end=" ")          

     

 