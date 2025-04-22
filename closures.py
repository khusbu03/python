# closures

def outterFunction(mssg):

    def innerFunction():
        print(f"Message is {mssg}")
        return "Executed inner Function"
    return innerFunction    

value=outterFunction("Hello! Khushi this side!")
print("value:",value)
print("value:",value())


def toPower(exponent):

    def calculateFunc(base):
        return base**exponent
    return calculateFunc

cubeFunction=toPower(3)    
value=cubeFunction(5)    
print("value of cube of 5 is",value)

squareFuction=toPower(2)
value=squareFuction(5)

print("Sqaure of 5 is",value)