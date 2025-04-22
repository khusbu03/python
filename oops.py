# oops
class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age

p1=Person("Khushi","Phulara",21)    

print(p1.firstName,p1.lastName)

class Laptop:
    def __init__(self,name,price):
        self.name=name
        self.price=price

laptop1=Laptop("Hp",52000)        

print(laptop1.name,laptop1.price)
# self refers to that instance of that circle
# class varibale is a  variable that is used for all the instances of that class

class Circle:

    # class variable
    pi=3.14
    count=0


# this is a class method ,and can be invoked only by using theb clas name
    @classmethod
    def countInstances(cls):
        # cls is referring to the class 
        return f"You have created {cls.count} instances of the {cls.__name__} class"

    @classmethod
    def objectInitilisation(cls,string):
        radius,diameter=string.split(',')
        return cls(radius,diameter)    

    # __init__ is the constructor that is use dto initialise the objects of a class
    def __init__(self,radius,diameter):
        Circle.count+=1
        self.radius=radius
        self.diameter=diameter

    def area(self):
        return Circle.pi*self.radius*self.radius

    def circumference(self):
        return 2*Circle.pi*self.radius


c1=Circle(4,8)
c2=Circle(2,4)


print("area of circle 1",c1.area())
print(Circle.count)
print("area of circle 1",c2.area())

#  __dict__ is used to get all the properties of  an object
print(c1.__dict__)
print(Circle.countInstances())
c3=Circle.objectInitilisation("4,8")
print(c3.area())

