# setter decorartor
# lrt suppose we have  a class Mobile where we have some parametrs like device name ,price 
#  now it is possible that user creates an instance of the mobile class where the value of the price given is less than 0 means 
#  it is neagtive in that case we should have something that sets the pice of the mobile to some default value insead of seeting it as negative
#  this is where we use teh setter decorartos we can do this by using the  i else condition
#  in the constructor which checks taht if the price of the mobile is less than 0 then it sets it to defaukt value





numbers=[32,54,65,43]

newList=[i+5 for i in numbers ]
print(newList)