# Generators are iterators

# iterator ,iterable

# below line is an example of iteable
arrList=[1,32,54,76,65]  

# for i in arrList:
#     print(i)

i=iter(arrList)  # thsi i is now an iterator 

print(next(i))  #1
print(next(i))  #32
print(next(i)) #54
print(next(i)) #76
print(next(i)) #65
# print(next(i))  this will give error no item to iterate
 

#  Alist requires to store all teh elements in te memory and then it will execute it
# and  genratos always stpre  a single value at one time so occupie sless memory thus more useful




class NewClass:
    @staticmethod
    def printHello():
        print("This is static method")