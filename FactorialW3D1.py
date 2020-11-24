
# Factorial of a number
num = int(input("Please Enter a number whose factorial you want"))
product=1
while (num>=1):
    product = num*product
    num = num-1
print("The Factorial is ",product)