# flexible functions
def total(a,b,c):
    return an+b+c

# total(2,3,45,6,6) =>this will give error because we are passing more parameters then expected
# so for this we have *args
# if i will use *args inside the prenthess of the function then i can give as many as parameters it will will be internally passed as a tuple''

# this args in sum function is a tuple basically,so we can iterate oerv the elements of the tuple and can perform the operation 
# def sum(*args):  sum(num,*args)=> in this function defination we have to pass atleast one parameter 
def sum(*args):
    sum=0
    print("args=>",args)
    for num in args:
        sum+=num

    print(sum)
    # print(type(args))

sum(2,4,3,4)

# when ever we want to pass a list as an argument and if we have passed args as an parameter in the function defination then in that case 
# if we will pass a list or a tuple it will be considered as a single element ,So, in that case we will pass the the list in arguments as *list

numbers=[2,32,45,67,8,65,87]
sum(*numbers)

def newSumFunction(num,*args):
    sum=num
    for i in  args:
        sum+=i
    return sum

value=newSumFunction(5,*numbers)        
print("value :",value)



# This kwargs will get the parameter as a dictionary
def func(nickName,**kwargs):
    for key,value in  kwargs.items():
        print(f"{key}:{value}")


func("Khusbu Phulara",first_name="Khushi",last_name="Phulara")    
# func("Khushi","Phulara")=>this will give error 

# now i i want to pass the dictionary as  the argumnet for eg> func(name,dict)=> then it will gie me error
# because it will not consider it as a dictioanary,so, we can pass the dictionary by unpacking
# For eg

dictionaryNew={
    "name":"Khusbu",
    "age":21,
    "hometown":"Uttrakhand"
}

func("Khushi",**dictionaryNew)
# Now this will not give error

# default order of using all the parmeters ,default parameters,args ,kwargs in  teh same function
# func(name,*args,last_name="Khushi",**kwargs)


def reverseAndCapitalizeFunction(list,reverseTrue):
    newList=[i.capitalize() for i in list]
    if(reverseTrue):
        newList.reverse()
    print("New String",newList) 

reverseAndCapitalizeFunction(["khushi","phulara","jyoti"],True)  
reverseAndCapitalizeFunction(["khushi","phulara","jyoti"],False)  
