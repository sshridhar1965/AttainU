
# CalculatorW2D51

print("Please select from following options")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Table of")
function=int(input())
if (function==1):
    
    a=input("Please Enter the first number")
    b=input("Please Enter the second number")
    c=int(a)+int(b)
    print("The sum is = ",c)
if (function==2):
    
    a=input("Please Enter the first number")
    b=input("Please Enter the second number")
    c=int(a)-int(b)
    print("The difference is = ",c)
if (function==3):
    
    a=input("Please Enter the first number")
    b=input("Please Enter the second number")
    c=int(a)*int(b)
    print("The product is = ",c)
if (function==4):
    
    a=input("Please Enter the first number")
    b=input("Please Enter the second number")
    c=int(a)/int(b)
    print("The result is = ",c)
if (function==5):
    
    a=input("Please Enter the number for which you want the table")
    for i in range(1,11):
        print(int(a)*i)