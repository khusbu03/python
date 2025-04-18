print("Heello world")
print("heello world2",23465)

name="Khushi Phulara"
age=21
gender="female"
weight=53.5
name=21
degree=None
print(name,age,gender,weight)
print(type(name))
print(type(age))
print(type(weight))
print(type(gender))
print(type(degree))
a=2
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#single line comment

print(float("2"))
print(int(4.0))

#typecasting only works when the data of that varible is capabl eof getting coverted in that data type
# For eg if we will try to convert the string "Khushi Phulara" into int or float then it will give error


# multi
# line
# comment

# input is use dto take the input from the user
# name=input("Enter your name :")
# age=int(input("Ente your age:"))
# weight=float(input("Enter your weight"))
# print("Welcome",name)
# print("Your age is :",age)
# print("Your gender is :",gender)

# num1=int(input("Enter first number"))
# num2=int(input("Enter second number"))
# print("sum:",num1+num2)


newAge=18

if(newAge==18):print("You can apply for liscence")
else: print("You can't drive")

numbers=[12.45,43,67,98,90]
numbers.append(878)

print(numbers)

newTuple=(345,76,76,321,876)
print(newTuple)
print(newTuple[0])
print(newTuple[1])
print(newTuple)

print(newTuple.index(345))
print(newTuple.count(76))

movies=[]
print(type("Khushi"))

# movie=str(input("Enter the name of the movie you like the most"))
# movies.append(movie)
# movie=str(input("One more"))
# movies.append(movie)
# movie=str(input("one more"))
# movies.append(movie)

print(movies)

# Dictonares are used to store key value pairs
dic={
    "name":"khushi",
    "age":78,
    "cllg":"UIET"
}
print(dic)
set1={45,65,34}
set2={34,45,34}
print(set1.union(set2))
print(set1.intersection(set2))

fruits={"apple","banana","pineapple","apple"}
print("fruits:",fruits)

score=None
marks={}

score=int(input("Enter your phy score: "))
marks.update({"phy":score})

score=int(input("Enter your che score: "))
marks.update({"che":score})

score=int(input("Enter your maths score: "))
marks.update({"maths":score})

print("Marks :",marks)

numbers={99,9,9.0,9.000,"9"}
print(numbers)
numbers={("int",9),("float",9.000),("string",'9.0000')}
print(numbers)


count=0

while(count<=5):
 print("count is :",count)
 count+=1

