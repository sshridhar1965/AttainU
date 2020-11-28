
# limit
def limit():
    a=int(input(" Please enter the number"))
    for i in range(0,a+1):
        if(i%2==0):
            print(i,"Even")
        else:
            print(i,"Odd")

    
limit()
