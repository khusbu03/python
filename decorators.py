# DEcoratoprs are basically used to incraease the functionality of nornaal functions 
#  for example let's suppose we have two function func1 and func2 and i want to add a print
#  line to both the fuunctions with fifferent value So, instaed of eperately adding the lines 
# to both the functions i can use decorator



# def func1():
#     print("This is function1")


# def func2():
#     print("This is function2")    

# def decoratorFunction(func):
#     def wrapperFunction():
#         print("This is the new print line that is added")
#         func()
#     return wrapperFunction;    

# newFunction=decoratorFunction(func1)
# newFunction()
# newFunction2=decoratorFunction(func2)
# newFunction2()





#  now instead of calling the decoratorFunction and then  again calling the function retruned by the 
# decorator funtion what we can do is we ca mention  in func1 and func2 that they are decorator function
# So it on invloking teh func1 and func2 it will automatically invoke the decorartor function for it

def decoratorFunction(func):
    def wrapperFunction(*args,**kwargs):
        print("This is the new print line that is added")
        func(*args,**kwargs)
    return wrapperFunction;   


@decoratorFunction    # this is shortcut   now when ever we will call func1 it will call decoratorFunction
def func1(num):
    print(f"This is function {num}")

@decoratorFunction
def func2(num):
    print(f"This is function {num}")    


func1(9)
func2(2)

# if i will pass any arguments then it will give me error 
# to resolve this we can us args and kwargs in the decoratroFunction


