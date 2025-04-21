# print("Heello world")
# print("heello world2",23465)

# name="Khushi Phulara"
# age=21
# gender="female"
# weight=53.5
# name=21
# degree=None
# print(name,age,gender,weight)
# print(type(name))
# print(type(age))
# print(type(weight))
# print(type(gender))
# print(type(degree))
# a=2
# b=4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# #single line comment

# print(float("2"))
# print(int(4.0))

# #typecasting only works when the data of that varible is capabl eof getting coverted in that data type
# # For eg if we will try to convert the string "Khushi Phulara" into int or float then it will give error


# # multi
# # line
# # comment

# # input is use dto take the input from the user
# # name=input("Enter your name :")
# # age=int(input("Ente your age:"))
# # weight=float(input("Enter your weight"))
# # print("Welcome",name)
# # print("Your age is :",age)
# # print("Your gender is :",gender)

# # num1=int(input("Enter first number"))
# # num2=int(input("Enter second number"))
# # print("sum:",num1+num2)


# newAge=18

# if(newAge==18):print("You can apply for liscence")
# else: print("You can't drive")

# numbers=[12.45,43,67,98,90]
# numbers.append(878)

# print(numbers)

# newTuple=(345,76,76,321,876)
# print(newTuple)
# print(newTuple[0])
# print(newTuple[1])
# print(newTuple)

# print(newTuple.index(345))
# print(newTuple.count(76))

# movies=[]
# print(type("Khushi"))

# # movie=str(input("Enter the name of the movie you like the most"))
# # movies.append(movie)
# # movie=str(input("One more"))
# # movies.append(movie)
# # movie=str(input("one more"))
# # movies.append(movie)

# print(movies)

# # Dictonares are used to store key value pairs
# dic={
#     "name":"khushi",
#     "age":78,
#     "cllg":"UIET"
# }
# print(dic)
# set1={45,65,34}
# set2={34,45,34}
# print(set1.union(set2))
# print(set1.intersection(set2))

# fruits={"apple","banana","pineapple","apple"}
# print("fruits:",fruits)

# score=None
# marks={}

# score=int(input("Enter your phy score: "))
# marks.update({"phy":score})

# score=int(input("Enter your che score: "))
# marks.update({"che":score})

# score=int(input("Enter your maths score: "))
# marks.update({"maths":score})

# print("Marks :",marks)

# numbers={99,9,9.0,9.000,"9"}
# print(numbers)
# numbers={("int",9),("float",9.000),("string",'9.0000')}
# print(numbers)


count=0

while(count<=5):
 print("count is :",count)
 count+=1

names=["Khushi","Aayushi","sapna"]

for name in names:
    print(name)
    if(name=="Aayushi"):
        print("My name is Anthony")
  
# count=0
# while count<=10:
#     print(count)
#     count+=1

squares=[]
for i in range(0,11):
    squares.append(i**2)

print("squares:",squares)   

newSquares=[i**2 for i in range(11)]
print("newSquares:",newSquares)

#  negative sqaures
negativeNumbers=[-i**2 for i in range(11)]
print("negativeNumbers:",negativeNumbers)

FirstLetterOfNames=[]

for name in names:
    FirstLetterOfNames.append(name[0])

print("array:",FirstLetterOfNames)    

FirstLetterOfNames= [name[0] for name in names]
print("new Aryay",FirstLetterOfNames)

newString=["abc","def","deg"]
newString.reverse()
print(newString)

# functions
def sum(a,b):
    return a+b

print(sum(1,3))

def factorial(n):
    if(n==1):return 1
    else :return n*factorial(n-1)

value=factorial(5)
print("vaue  of factorial:",value)


def average(x,y,z):
    return (x+y+z)/3

print(int(average(3,3,3)))    

# built in functions => print ,len,range()

print("print build in function:","this is value",sep="-",end="*")
# sep is used to seperate two values in the print function by default value in print built in function is space and end is used that how we wnat our output to end with
#  in print end by deault value is "*"

def newFunction(a,b=2):
    return a*b

print(newFunction(1))
print("value",newFunction(2))

numbers=[43,542,21]

def lengthOfList(arrayList):
    return len(arrayList)


# print("The length of the names list ",lengthOfList(numbers))
# for num in numbers:
#     print(num,end=" ")

numbers=list(range(1,11))
print(numbers)

evenNumbers=list( i for i in numbers if i%2==0)
evenNumbers2=list( i for i in range(1,11) if i%2==0)
oddNumbers=[i for i in  numbers if i%2!=0]
print("even Numbers",evenNumbers)
print("even Numbers",evenNumbers2)
print("odd Numbers",oddNumbers)

randomString=[True,False,1,1.0,[1,2,3],2,3,34]

newString =[str(i) for i in randomString if(type(i)==int or type(i)==float)]
print("new String from the random string",newString)

evenNumbersSquare=[i**2 for i in numbers if i%2==0]
evenNumbersSquare2=[i**2 if i%2==0 else -i for i in numbers ]
print("evenNumbersSquare",evenNumbersSquare)
print("evenNumbersSquare",evenNumbersSquare2)

for i in range(0,3):
    for j in range(0,3):
        print("value if i and j ",i,j)


# Nested list comprehension
# example=> [[1,32,43],[43,54,765]]

# target list => [[1,2,3],[1,2,3],[1,2,3]]
targetList=[]
for i in range(0,3):
    subList=[]
    for j in range(0,3):
        # print("i:",i,"j:",j)
        subList.append(j)
    targetList.append(subList)  

targetList2=[[i for i in range(0,3)] for j in range(0,3)]  

print("targetList",targetList)
print("targetList2",targetList2)


