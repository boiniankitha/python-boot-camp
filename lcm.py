a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
while b!=0:
    a,b=b,a*b
lcm = a*b/a
print("lcm of two numbers is:",a)
