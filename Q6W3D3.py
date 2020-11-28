
# Pattern
def pattern():
    aster = "*"
    inp=int(input("Please enter the number for how many lines you want the pattern"))
    for i in range (1,inp+1):
        print (aster)
        aster=aster+"*"
        inp=inp-1
pattern()